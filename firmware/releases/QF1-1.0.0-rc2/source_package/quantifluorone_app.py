import gc
import json
import math
import os
import sys
import time
import board
import displayio
import keypad
import terminalio
from adafruit_display_text import label
import adafruit_tca9548a
import adafruit_tsl2591

if "/src" not in sys.path:
    sys.path.append("/src")
import constants

VERSION = "QF1-1.0.0-rc2"
DISPLAY_VERSION = "v1.0 RC2"
CONFIG_FILE = "/quantifluorone_config.json"
STATE_FILE = "/quantifluorone_state.json"
CAL_FILE = "/quantifluorone_calibration.json"
MP_FILE = "/quantifluorone_multipoint.json"
LOG_FILE = "/quantifluorone_log_v100rc2.csv"
MENU = ("2-PT CAL", "10-BLANK L/Q", "LOAD MP CAL", "CAL STATUS", "CLEAR CAL")
GAIN = {
    "low": adafruit_tsl2591.GAIN_LOW,
    "med": adafruit_tsl2591.GAIN_MED,
    "high": adafruit_tsl2591.GAIN_HIGH,
    "max": adafruit_tsl2591.GAIN_MAX,
}
ITIME = {
    100: adafruit_tsl2591.INTEGRATIONTIME_100MS,
    200: adafruit_tsl2591.INTEGRATIONTIME_200MS,
    300: adafruit_tsl2591.INTEGRATIONTIME_300MS,
    400: adafruit_tsl2591.INTEGRATIONTIME_400MS,
    500: adafruit_tsl2591.INTEGRATIONTIME_500MS,
    600: adafruit_tsl2591.INTEGRATIONTIME_600MS,
}


def fmt(value):
    if value is None:
        return "n/a"
    value = float(value)
    if abs(value) >= 1000:
        return "%.0f" % value
    if abs(value) >= 100:
        return "%.1f" % value
    if abs(value) >= 10:
        return "%.2f" % value
    if abs(value) >= 0.01 or value == 0:
        return "%.3f" % value
    return "%.2e" % value


def raw(value):
    return "-" if value is None else str(int(round(value)))


def cv(mean, sd):
    if mean in (None, 0) or sd is None:
        return 0.0
    return abs(sd / mean) * 100.0


def stats3(values):
    mean = (values[0] + values[1] + values[2]) / 3.0
    sd = math.sqrt(
        ((values[0] - mean) ** 2 + (values[1] - mean) ** 2 + (values[2] - mean) ** 2) / 2.0
    )
    return mean, sd


def stats_n(values):
    count = len(values)
    mean = sum(values) / count
    sd = math.sqrt(sum((value - mean) ** 2 for value in values) / (count - 1))
    return mean, sd


class Screen:
    Y = (10, 27, 44, 61, 78, 95, 115)
    Y2 = (16, 37, 58, 79, 100, 121)

    def __init__(self):
        display = board.DISPLAY
        bitmap = displayio.Bitmap(1, 1, 1)
        palette = displayio.Palette(1)
        palette[0] = 0
        bg = displayio.Group(scale=max(display.width, display.height))
        bg.append(displayio.TileGrid(bitmap, pixel_shader=palette))
        self.group = displayio.Group()
        self.group.append(bg)
        self.labels = []
        colors = (0xFFFFFF, 0xA7D8FF, 0xFFB347, 0xFFFFFF, 0xB8B8B8, 0x7FDBFF, 0x888888)
        for i in range(7):
            item = label.Label(terminalio.FONT, text="", color=colors[i], x=4, y=self.Y[i])
            self.labels.append(item)
            self.group.append(item)
        display.root_group = self.group

    def show(self, lines, large=False):
        ys = self.Y2 if large else self.Y
        scale = 2 if large else 1
        width = 12 if large else 25
        for i, item in enumerate(self.labels):
            if i < len(ys):
                item.x = 4
                item.y = ys[i]
                item.scale = scale
                item.text = str(lines[i])[:width] if i < len(lines) else ""
            else:
                item.text = ""


class QuantiFluorOneApp:
    def __init__(self):
        self.screen = Screen()
        self.screen.show(("QuantiFluorONE", VERSION, "Starting...", "", "", "", ""))
        gc.collect()
        cfg = self._read_json(CONFIG_FILE, True)
        hw = cfg.get("hardware", {})
        meas = cfg.get("measurement", {})
        samples = cfg.get("samples", {})
        cal = cfg.get("two_point_calibration", {})
        limits = cfg.get("blank_limit_study", {})
        mp = cfg.get("multipoint_import", {})
        assay = cfg.get("assay", {})
        self.mux_address = int(hw.get("mux_address", 112))
        self.sensor_address = int(hw.get("sensor_address", 41))
        self.requested_channel = hw.get("sensor_channel", None)
        self.allow_direct = bool(hw.get("allow_direct_sensor", True))
        self.gain_name = str(hw.get("gain", "max")).lower()
        self.integration_ms = int(hw.get("integration_time_ms", 600))
        self.settle_s = float(meas.get("settle_s", 0.65))
        self.overflow = int(meas.get("overflow_threshold", 65000))
        self.csv_logging = bool(meas.get("csv_logging", True))
        self.sample_list = list(samples.get("list", ("Sample01",)))
        if not self.sample_list:
            self.sample_list = ["Sample01"]
        self.std_values = list(cal.get("standard_concentrations_ng_uL", (1, 5, 10, 20, 40, 100, 200, 400)))
        if not self.std_values:
            self.std_values = [400.0]
        self.min_rfu = float(cal.get("minimum_rfu", 5.0))
        self.max_cv = float(cal.get("maximum_cv_percent", 5.0))
        self.min_snr = float(cal.get("minimum_snr", 3.0))
        self.near_fraction = float(cal.get("near_saturation_fraction", 0.95))
        self.limit_count = max(3, int(limits.get("blank_count", 10)))
        self.lod_sigma = float(limits.get("lod_sigma", 3.0))
        self.loq_sigma = float(limits.get("loq_sigma", 10.0))
        self.mp_file = str(mp.get("file", MP_FILE))
        self.default_dilution = float(assay.get("dilution_factor", 201.0))
        del cfg, hw, meas, samples, cal, limits, mp, assay
        gc.collect()

        if self.gain_name not in GAIN or self.integration_ms not in ITIME:
            raise RuntimeError("Invalid sensor setting")

        state = self._read_json(STATE_FILE, False)
        self.sample_index = int(state.get("sample_index", 0)) % len(self.sample_list)
        self.std_index = int(state.get("standard_index", len(self.std_values) - 1)) % len(self.std_values)
        self.blank_mean = state.get("blank_mean", None)
        self.blank_sd = state.get("blank_sd", None)
        self.blank_channel = state.get("blank_channel", None)
        self.blank_gain = state.get("blank_gain", None)
        self.blank_itime = state.get("blank_itime", None)
        self.cal_valid = bool(state.get("calibration_valid", False))
        del state

        self.cal_enabled = False
        self.cal_type = None
        self.cal_model = "-"
        self.cal_id = "-"
        self.cal_standard = None
        self.cal_intercept = 0.0
        self.cal_slope = None
        self.cal_type = None
        self.cal_lod = self.cal_loq = None
        self.ci_low = self.ci_high = None
        self.cal_rfu = None
        self.cal_std_mean = None
        self.cal_std_sd = None
        self.cal_qc = "-"
        self.cal_r2 = None
        self.cal_syx = None
        self.cal_n = None
        self.cal_xbar = None
        self.cal_sxx = None
        self.cal_t = None
        self.cal_alpha = None
        self.cal_ci_percent = 95
        self.cal_lod = None
        self.cal_loq = None
        self.cal_status = "NONE"
        self.cal_dilution = 1.0
        self.cal_x_min = None
        self.cal_x_max = None
        self.result_flag = ""
        self.limit_n = 0
        self.limit_mean = None
        self.limit_sd = None

        self.full = [0.0, 0.0, 0.0]
        self.ir = [0.0, 0.0, 0.0]
        self.vis = [0.0, 0.0, 0.0]
        self.full_mean = self.full_sd = None
        self.ir_mean = self.ir_sd = None
        self.vis_mean = self.vis_sd = None
        self.rfu = self.concentration = None
        self.ci_low = self.ci_high = None
        self.last_kind = None
        self.status = "Ready"
        self.mode = "live"
        self.page = 0
        self.menu_index = 0
        self.cal_blank = None
        self.cal_standard_data = None
        self.candidate_slope = None
        self.candidate_rfu = None
        self.candidate_qc = "-"
        self.limit_values = []
        self.fs_status = ""

        self.i2c = board.I2C()
        self.mux = None
        self.sensor = None
        self.sensor_channel = None
        self.hardware_mode = "unknown"
        self._setup_sensor()
        self._load_calibration()
        self._validate_blank()
        self._setup_buttons()
        self._update()
        gc.collect()

    @property
    def sample_id(self):
        return self.sample_list[self.sample_index]

    @staticmethod
    def _read_json(path, required):
        try:
            with open(path, "r") as file_obj:
                value = json.load(file_obj)
            return value if isinstance(value, dict) else {}
        except (OSError, ValueError):
            if required:
                raise RuntimeError("Missing/invalid config")
            return {}

    @staticmethod
    def _scan(bus):
        while not bus.try_lock():
            pass
        try:
            return list(bus.scan())
        finally:
            bus.unlock()

    def _setup_sensor(self):
        main = self._scan(self.i2c)
        found = []
        if self.mux_address in main:
            self.mux = adafruit_tca9548a.PCA9546A(self.i2c, address=self.mux_address)
            channels = (int(self.requested_channel),) if self.requested_channel is not None else range(4)
            for channel in channels:
                if self.sensor_address in self._scan(self.mux[channel]):
                    found.append(channel)
            if len(found) != 1:
                raise RuntimeError("Need exactly one TSL2591")
            self.sensor_channel = found[0]
            self.sensor = adafruit_tsl2591.TSL2591(self.mux[self.sensor_channel])
            self.hardware_mode = "mux"
        elif self.allow_direct and self.sensor_address in main:
            self.sensor_channel = -1
            self.sensor = adafruit_tsl2591.TSL2591(self.i2c)
            self.hardware_mode = "direct"
        else:
            raise RuntimeError("TSL2591 not found")
        self.sensor.gain = GAIN[self.gain_name]
        self.sensor.integration_time = ITIME[self.integration_ms]
        self.status = "Sensor CH%s ready" % self.sensor_channel

    def _same_context(self, channel, gain, itime):
        try:
            return int(channel) == int(self.sensor_channel) and str(gain) == self.gain_name and int(itime) == self.integration_ms
        except (TypeError, ValueError):
            return False

    def _validate_blank(self):
        if self.blank_mean is None:
            return
        if not self._same_context(self.blank_channel, self.blank_gain, self.blank_itime):
            self.blank_mean = self.blank_sd = None
            if self.cal_type == "two_point":
                self.cal_valid = False
                self.cal_enabled = False
            self.status = "Blank reset: sensor cfg"

    @staticmethod
    def _write_json(path, data):
        try:
            with open(path + ".tmp", "w") as file_obj:
                json.dump(data, file_obj)
            try:
                os.remove(path)
            except OSError:
                pass
            os.rename(path + ".tmp", path)
            return True
        except OSError:
            return False

    def _load_calibration(self):
        data = self._read_json(CAL_FILE, False)
        if not data.get("enabled", False):
            self.cal_valid = False
            return
        if not self._same_context(data.get("sensor_channel"), data.get("gain"), data.get("integration_time_ms")):
            self.cal_valid = False
            self.status = "Calibration reset"
            return
        try:
            cal_type = str(data.get("type", "two_point"))
            slope = float(data.get("slope_rfu_per_ng_uL"))
            if slope <= 0:
                raise ValueError
            self.cal_type = cal_type
            self.cal_slope = slope
            self.cal_intercept = float(data.get("intercept_rfu", 0.0))
            self.cal_model = str(data.get("model", "2-point" if cal_type == "two_point" else "OLS"))
            self.cal_id = str(data.get("calibration_id", "-"))
            self.cal_lod = data.get("lod_ng_uL", None)
            self.cal_loq = data.get("loq_ng_uL", None)
            self.cal_status = str(data.get("calibration_status", "ACTIVE")).upper()
            self.cal_dilution = float(data.get("dilution_factor", self.default_dilution))
            self.cal_x_min = data.get("range_min_ng_uL", None)
            self.cal_x_max = data.get("range_max_ng_uL", None)
            self.cal_qc = str(data.get("qc", "-"))
            self.cal_r2 = data.get("r_squared", None)
            self.limit_n = int(data.get("limit_blank_n", 0))
            self.limit_mean = data.get("limit_blank_mean", None)
            self.limit_sd = data.get("limit_blank_sd", None)
            if cal_type == "two_point":
                self.cal_standard = float(data.get("standard_ng_uL"))
                self.cal_rfu = float(data.get("standard_rfu"))
                self.cal_std_mean = float(data.get("standard_mean"))
                self.cal_std_sd = float(data.get("standard_sd"))
            elif cal_type == "multipoint":
                self.cal_syx = float(data.get("residual_sd_rfu"))
                self.cal_n = int(data.get("n_calibration"))
                self.cal_xbar = float(data.get("mean_concentration_ng_uL"))
                self.cal_sxx = float(data.get("sxx_concentration2"))
                self.cal_t = float(data.get("t_factor_two_sided"))
                self.cal_alpha = float(data.get("alpha", 0.05))
                self.cal_ci_percent = int(round((1.0 - self.cal_alpha) * 100.0))
                if self.cal_syx < 0 or self.cal_n <= 2 or self.cal_sxx <= 0 or self.cal_t <= 0:
                    raise ValueError
            else:
                raise ValueError
            self.cal_enabled = True
            self.cal_valid = True
        except (TypeError, ValueError):
            self.cal_valid = False
            self.cal_enabled = False
            self.cal_type = None

    def _setup_buttons(self):
        for name in ("menu", "norm", "itime", "gain", "up", "down", "right"):
            if name not in constants.BUTTON:
                raise RuntimeError("Missing button " + name)
        self.left_key = constants.BUTTON.get("left", None)
        self.pad = keypad.ShiftRegisterKeys(
            clock=board.BUTTON_CLOCK,
            data=board.BUTTON_OUT,
            latch=board.BUTTON_LATCH,
            key_count=8,
            value_when_pressed=True,
        )

    def _read_sensor(self):
        last_error = None
        for _ in range(4):
            try:
                try:
                    value = self.sensor.raw_luminosity
                    full, ir = float(value[0]), float(value[1])
                except AttributeError:
                    full = float(self.sensor.full_spectrum)
                    ir = float(self.sensor.infrared)
                if full >= self.overflow or ir >= self.overflow:
                    raise RuntimeError("TSL2591 saturation")
                return full, ir
            except RuntimeError:
                raise
            except (OSError, ValueError, TypeError) as error:
                last_error = error
                time.sleep(0.12)
        if last_error is not None:
            raise last_error
        raise RuntimeError("TSL2591 read failed")

    def _acquire(self, title):
        gc.collect()
        wait_s = max(self.settle_s, self.integration_ms / 1000.0 + 0.05)
        for i in range(3):
            self.screen.show((title, "Reading %d/3" % (i + 1), "", "", "", "", ""))
            time.sleep(wait_s)
            full, ir = self._read_sensor()
            self.full[i] = full
            self.ir[i] = ir
            self.vis[i] = max(full - ir, 0.0)
        self.full_mean, self.full_sd = stats3(self.full)
        self.ir_mean, self.ir_sd = stats3(self.ir)
        self.vis_mean, self.vis_sd = stats3(self.vis)
        self.rfu = None if self.blank_mean is None else self.vis_mean - self.blank_mean
        self.concentration = None
        self.ci_low = self.ci_high = None
        self.result_flag = ""
        self._predict()

    def _predict(self):
        self.ci_low = self.ci_high = None
        if not self.cal_enabled or self.rfu is None or not self.cal_slope:
            return
        self.concentration = (self.rfu - self.cal_intercept) / self.cal_slope
        self.result_flag = ""
        if self.cal_x_min is not None and self.concentration < float(self.cal_x_min):
            self.result_flag = "BELOW RANGE"
        elif self.cal_x_max is not None and self.concentration > float(self.cal_x_max):
            self.result_flag = "ABOVE RANGE"
        if self.cal_type != "multipoint":
            return
        try:
            syx = float(self.cal_syx)
            slope = abs(float(self.cal_slope))
            count = float(self.cal_n)
            xbar = float(self.cal_xbar)
            sxx = float(self.cal_sxx)
            t_value = abs(float(self.cal_t))
            if slope <= 0 or count <= 2 or sxx <= 0 or syx < 0 or t_value <= 0:
                return
            variance_term = (
                1.0
                + 1.0 / count
                + ((self.concentration - xbar) ** 2) / sxx
            )
            if variance_term < 0:
                return
            half = t_value * (syx / slope) * math.sqrt(variance_term)
            self.ci_low = self.concentration - half
            self.ci_high = self.concentration + half
        except (TypeError, ValueError, ZeroDivisionError, OverflowError):
            self.ci_low = self.ci_high = None

    def measure_sample(self):
        self._acquire("MEASURE " + self.sample_id)
        self.last_kind = "sample"
        # Recalculate immediately before logging and display. This makes the
        # interval independent of any prior screen or menu state.
        self._predict()
        self._log("sample", self.sample_id)
        self.status = self.fs_status or "Sample saved"
        self.mode = "live"
        self._update()

    def measure_blank(self):
        self._acquire("REAGENT BLANK")
        self.blank_mean = self.vis_mean
        self.blank_sd = self.vis_sd
        self.blank_channel = self.sensor_channel
        self.blank_gain = self.gain_name
        self.blank_itime = self.integration_ms
        self.rfu = 0.0
        self.concentration = None
        self.ci_low = self.ci_high = None
        self.result_flag = ""
        self.last_kind = "blank"
        if self.cal_type == "two_point":
            self.cal_enabled = False
            self.cal_valid = False
            try:
                os.remove(CAL_FILE)
            except OSError:
                pass
            self.status = "Blank saved; recalibrate"
        else:
            self.status = "Blank saved"
        self._save_state()
        self._log("blank", "ReagentBlank")
        self.status = self.fs_status or self.status
        self.mode = "live"
        self._update()

    def _start_calibration(self):
        self.cal_blank = None
        self.cal_standard_data = None
        self.candidate_slope = None
        self.candidate_rfu = None
        self.candidate_qc = "-"
        self.mode = "cal_blank"
        self.page = 0
        self._update()

    def _measure_cal_blank(self):
        self._acquire("CAL BLANK")
        self.cal_blank = (self.vis_mean, self.vis_sd, max(self.full))
        self.rfu = 0.0
        self.concentration = None
        self.last_kind = "cal_blank"
        self._log("calibration_blank", "ReagentBlank")
        self.mode = "cal_select"
        self._update()

    def _measure_cal_standard(self):
        self._acquire("CAL STANDARD")
        standard = float(self.std_values[self.std_index])
        blank_mean, blank_sd, blank_peak = self.cal_blank
        rfu = self.vis_mean - blank_mean
        if standard <= 0 or rfu <= self.min_rfu:
            self.status = "INVALID: standard signal"
            self.mode = "cal_standard"
            self._update()
            return
        slope = rfu / standard
        noise = math.sqrt(blank_sd * blank_sd + self.vis_sd * self.vis_sd)
        snr = 999.0 if noise == 0 else rfu / noise
        warnings = ""
        if cv(blank_mean, blank_sd) > self.max_cv or cv(self.vis_mean, self.vis_sd) > self.max_cv:
            warnings += "CV "
        if snr < self.min_snr:
            warnings += "SNR "
        if max(blank_peak, max(self.full)) >= self.overflow * self.near_fraction:
            warnings += "SAT"
        self.candidate_qc = warnings.strip() or "OK"
        self.candidate_rfu = rfu
        self.candidate_slope = slope
        self.cal_standard_data = (self.vis_mean, self.vis_sd, max(self.full))
        self.rfu = rfu
        self.concentration = standard
        self.last_kind = "cal_standard"
        self._log("calibration_standard", "Std" + fmt(standard))
        self.mode = "cal_review"
        self.page = 0
        self._update()

    def _save_calibration(self):
        standard = float(self.std_values[self.std_index])
        blank_mean, blank_sd, blank_peak = self.cal_blank
        standard_mean, standard_sd, standard_peak = self.cal_standard_data
        data = {
            "enabled": True,
            "firmware_version": VERSION,
            "type": "two_point",
            "model": "blank_plus_standard",
            "calibration_id": "QF1-2PT",
            "standard_ng_uL": standard,
            "blank_mean": blank_mean,
            "blank_sd": blank_sd,
            "standard_mean": standard_mean,
            "standard_sd": standard_sd,
            "standard_rfu": self.candidate_rfu,
            "intercept_rfu": 0.0,
            "slope_rfu_per_ng_uL": self.candidate_slope,
            "lod_ng_uL": None,
            "loq_ng_uL": None,
            "limit_blank_n": 0,
            "calibration_status": "ACTIVE",
            "dilution_factor": self.default_dilution,
            "range_min_ng_uL": 0.0,
            "range_max_ng_uL": standard,
            "qc": self.candidate_qc,
            "sensor_channel": self.sensor_channel,
            "gain": self.gain_name,
            "integration_time_ms": self.integration_ms,
        }
        if not self._write_json(CAL_FILE, data):
            self.status = "Calibration write failed"
            self.mode = "cal_review"
            self._update()
            return
        self.blank_mean = blank_mean
        self.blank_sd = blank_sd
        self.blank_channel = self.sensor_channel
        self.blank_gain = self.gain_name
        self.blank_itime = self.integration_ms
        self.cal_type = "two_point"
        self.cal_model = "blank+standard"
        self.cal_id = "QF1-2PT"
        self.cal_standard = standard
        self.cal_intercept = 0.0
        self.cal_slope = self.candidate_slope
        self.cal_rfu = self.candidate_rfu
        self.cal_std_mean = standard_mean
        self.cal_std_sd = standard_sd
        self.cal_qc = self.candidate_qc
        self.cal_status = "ACTIVE"
        self.cal_dilution = self.default_dilution
        self.cal_x_min = 0.0
        self.cal_x_max = standard
        self.cal_lod = self.cal_loq = None
        self.limit_n = 0
        self.limit_mean = self.limit_sd = None
        self.cal_enabled = True
        self.cal_valid = True
        self._save_state()
        self.status = "2-point calibration active"
        self.mode = "live"
        self._update()

    def _import_multipoint(self):
        data = self._read_json(self.mp_file, False)
        try:
            if str(data.get("calibration_mode", "")).lower() != "multipoint":
                raise ValueError
            model = str(data.get("calibration_model", "OLS"))
            if model.upper() != "OLS":
                raise ValueError
            mp = data.get("multipoint", {})
            slope = float(mp.get("slope_signal_per_x"))
            intercept = float(mp.get("intercept_signal"))
            syx = float(data.get("residual_sd_signal"))
            n_cal = int(mp.get("n_replicates"))
            xbar = float(mp.get("mean_concentration"))
            sxx = float(mp.get("sxx_concentration2"))
            t_value = float(mp.get("t_factor_two_sided"))
            if slope <= 0 or syx < 0 or n_cal <= 2 or sxx <= 0 or t_value <= 0:
                raise ValueError
            normalized = {
                "enabled": True,
                "firmware_version": VERSION,
                "type": "multipoint",
                "model": model,
                "calibration_id": str(data.get("calibration_id", "-")),
                "intercept_rfu": intercept,
                "slope_rfu_per_ng_uL": slope,
                "residual_sd_rfu": syx,
                "n_calibration": n_cal,
                "mean_concentration_ng_uL": xbar,
                "sxx_concentration2": sxx,
                "t_factor_two_sided": t_value,
                "alpha": float(data.get("alpha", 0.05)),
                "r_squared": data.get("r_squared", None),
                "lod_ng_uL": data.get("lod_x", None),
                "loq_ng_uL": data.get("loq_x", None),
                "calibration_status": str(data.get("calibration_status", "ACTIVE")).upper(),
                "dilution_factor": float(data.get("dilution_factor", 1.0)),
                "range_min_ng_uL": data.get("range_min_ng_uL", None),
                "range_max_ng_uL": data.get("range_max_ng_uL", None),
                "qc": "IMPORTED",
                "sensor_channel": self.sensor_channel,
                "gain": self.gain_name,
                "integration_time_ms": self.integration_ms,
            }
        except (TypeError, ValueError):
            self.status = "Invalid MP JSON"
            self.mode = "menu"
            self._update()
            return
        if not self._write_json(CAL_FILE, normalized):
            self.status = "MP calibration write failed"
            self.mode = "menu"
            self._update()
            return
        self._load_calibration()
        self._save_state()
        self.status = "MP loaded; measure blank" if self.blank_mean is None else "Multipoint active"
        self.mode = "live"
        self._update()

    def _start_limits(self):
        if not self.cal_enabled or self.cal_type != "two_point":
            self.status = "2-point calibration needed"
            self.mode = "menu"
            self._update()
            return
        self.limit_values = []
        self.mode = "limit"
        self._update()

    def _measure_limit_blank(self):
        number = len(self.limit_values) + 1
        self._acquire("LIMIT BLANK %d/%d" % (number, self.limit_count))
        self.limit_values.append(self.vis_mean)
        self.last_kind = "limit_blank"
        self._log("limit_blank", "Blank%02d" % number)
        if len(self.limit_values) >= self.limit_count:
            self.limit_mean, self.limit_sd = stats_n(self.limit_values)
            self.cal_lod = self.lod_sigma * self.limit_sd / self.cal_slope
            self.cal_loq = self.loq_sigma * self.limit_sd / self.cal_slope
            dilution = self.cal_dilution or self.default_dilution
            self.limit_n = len(self.limit_values)
            self.mode = "limit_result"
        self._update()

    def _save_limits(self):
        data = self._read_json(CAL_FILE, False)
        if data.get("type") != "two_point":
            self.status = "2-point calibration missing"
            self.mode = "menu"
            self._update()
            return
        data["lod_ng_uL"] = self.cal_lod
        data["loq_ng_uL"] = self.cal_loq
        data["limit_blank_n"] = self.limit_n
        data["limit_blank_mean"] = self.limit_mean
        data["limit_blank_sd"] = self.limit_sd
        data["limit_method"] = "%ssigma/%ssigma" % (fmt(self.lod_sigma), fmt(self.loq_sigma))
        if not self._write_json(CAL_FILE, data):
            self.status = "Limit write failed"
            self.mode = "limit_result"
            self._update()
            return
        self.status = "LOD/LOQ estimates saved"
        self.mode = "live"
        self._update()

    def _clear_calibration(self):
        self.cal_enabled = False
        self.cal_valid = False
        self.cal_type = None
        self.cal_slope = None
        self.cal_intercept = 0.0
        self.cal_lod = self.cal_loq = None
        self.cal_status = "NONE"
        self.cal_x_min = self.cal_x_max = None
        self.result_flag = ""
        self.ci_low = self.ci_high = None
        self._save_state()
        try:
            os.remove(CAL_FILE)
        except OSError:
            pass
        self.status = "Calibration cleared"
        self.mode = "menu"
        self._update()

    def _save_state(self):
        data = {
            "sample_index": self.sample_index,
            "standard_index": self.std_index,
            "blank_mean": self.blank_mean,
            "blank_sd": self.blank_sd,
            "blank_channel": self.blank_channel,
            "blank_gain": self.blank_gain,
            "blank_itime": self.blank_itime,
            "calibration_valid": self.cal_valid,
        }
        try:
            with open(STATE_FILE, "w") as file_obj:
                json.dump(data, file_obj)
            self.fs_status = "saved"
            return True
        except OSError as error:
            self.fs_status = "FS read-only" if error.args and error.args[0] == 30 else "write error"
            return False

    def _result_line(self):
        if self.cal_enabled and self.concentration is not None:
            suffix = " PROV" if self.cal_status.startswith("PROV") else ""
            if self.result_flag:
                suffix += " !"
            return "c=%s ng/uL%s" % (fmt(self.concentration), suffix)
        if self.cal_enabled:
            tag = "PROV" if self.cal_status.startswith("PROV") else "ACTIVE"
            return "cal=%s c=not measured" % tag
        return "cal=none c=uncalibrated"

    def _interval_line(self):
        if self.result_flag:
            return self.result_flag
        if self.concentration is not None and self.cal_type == "multipoint":
            if self.ci_low is not None and self.ci_high is not None:
                half = (self.ci_high - self.ci_low) / 2.0
                return "%d%% PI +/- %s" % (self.cal_ci_percent, fmt(half))
            return "%d%% PI unavailable" % self.cal_ci_percent
        if self.cal_lod is not None and self.cal_loq is not None:
            return "LOD %s LOQ %s" % (fmt(self.cal_lod), fmt(self.cal_loq))
        return "No interval/limits"

    def _raw_values(self, index):
        return ("%d F%s" % (index + 1, raw(self.full[index])), "I%s V%s" % (raw(self.ir[index]), raw(self.vis[index])))

    def _update(self):
        if self.mode == "live":
            self.screen.show((
                "QuantiFluorONE " + DISPLAY_VERSION,
                "Sample: " + self.sample_id,
                self._result_line(),
                self._interval_line(),
                "VIS=%s SD=%s" % (fmt(self.vis_mean), fmt(self.vis_sd)),
                "Blank=%s RFU=%s" % (fmt(self.blank_mean), fmt(self.rfu)),
                "A:sample START:blank",
            ))
        elif self.mode == "details":
            self.screen.show((
                "DETAILS " + (self.cal_type or "no-cal"),
                "FULL=%s SD=%s" % (fmt(self.full_mean), fmt(self.full_sd)),
                "IR=%s SD=%s" % (fmt(self.ir_mean), fmt(self.ir_sd)),
                "VIS=%s SD=%s" % (fmt(self.vis_mean), fmt(self.vis_sd)),
                "RFU=%s c=%s" % (fmt(self.rfu), fmt(self.concentration)),
                "CH%s %s %dms" % (self.sensor_channel, self.gain_name, self.integration_ms),
                "B:next RIGHT:raw",
            ))
        elif self.mode == "raw":
            if self.page == 0:
                a = self._raw_values(0)
                b = self._raw_values(1)
                lines = (self.sample_id[:8] + " 1/2", a[0], a[1], b[0], b[1], "LEFT:page2")
            else:
                c = self._raw_values(2)
                peak = max(self.full)
                sat = "NEAR" if peak >= self.overflow * self.near_fraction else "OK"
                lines = (self.sample_id[:7] + " 2 " + sat, c[0], c[1], "M " + fmt(self.vis_mean), "SD%s P%s" % (fmt(self.vis_sd), raw(peak)), "LEFT:page1")
            self.screen.show(lines, True)
        elif self.mode == "menu":
            lines = ["SELECT MENU"]
            for i, text in enumerate(MENU):
                lines.append((">" if i == self.menu_index else " ") + text)
            lines.append("SEL:open B:back")
            self.screen.show(tuple(lines))
        elif self.mode == "cal_blank":
            self.screen.show(("CALIBRATION 1/2", "Insert reagent blank", "Press START", "Triplicate reading", "", "", "B:cancel"))
        elif self.mode == "cal_select":
            self.screen.show(("HIGH STANDARD", fmt(self.std_values[self.std_index]) + " ng/uL", "UP/DOWN:change", "SELECT:continue", "Blank=" + fmt(self.cal_blank[0]), "SD=" + fmt(self.cal_blank[1]), "B:cancel"))
        elif self.mode == "cal_standard":
            self.screen.show(("CALIBRATION 2/2", "Insert " + fmt(self.std_values[self.std_index]), "ng/uL standard", "Press A", "Triplicate reading", self.status, "B:cancel"))
        elif self.mode == "cal_review":
            if self.page == 0:
                lines = ("CAL RESULT 1/2", "Blank M " + fmt(self.cal_blank[0]), "Blank SD " + fmt(self.cal_blank[1]), "Std M " + fmt(self.cal_standard_data[0]), "Std SD " + fmt(self.cal_standard_data[1]), "LEFT:page2", "SEL:save B:cancel")
            else:
                lines = ("CAL RESULT 2/2", "RFU " + fmt(self.candidate_rfu), "Slope " + fmt(self.candidate_slope), "QC " + self.candidate_qc, "Std " + fmt(self.std_values[self.std_index]), "LEFT:page1", "SEL:save B:cancel")
            self.screen.show(lines)
        elif self.mode == "limit":
            number = len(self.limit_values) + 1
            self.screen.show(("10-BLANK LOD/LOQ", "Independent blank", "%d of %d" % (number, self.limit_count), "Insert fresh blank", "Press START", "Saved: %d" % len(self.limit_values), "B:cancel"))
        elif self.mode == "limit_result":
            self.screen.show(("BLANK LIMIT RESULT", "n=%d mean=%s" % (self.limit_n, fmt(self.limit_mean)), "SD=%s RFU" % fmt(self.limit_sd), "LOD=%s ng/uL" % fmt(self.cal_lod), "LOQ=%s ng/uL" % fmt(self.cal_loq), "3.3sigma / 10sigma", "SEL:save B:cancel"))
        elif self.mode == "cal_status":
            if not self.cal_enabled:
                self.screen.show(("CAL STATUS", "No active calibration", "", "", "", "", "SELECT/B:back"))
            elif self.cal_type == "multipoint" and self.page == 0:
                self.screen.show(("MP CAL STATUS 1/2", "Status " + self.cal_status[:12], "Model " + self.cal_model, "a " + fmt(self.cal_intercept), "b " + fmt(self.cal_slope), "R2 " + fmt(self.cal_r2), "LEFT:page2"))
            elif self.cal_type == "multipoint":
                self.screen.show(("MP CAL STATUS 2/2", "Range %s..%s" % (fmt(self.cal_x_min), fmt(self.cal_x_max)), "syx %s N %s" % (fmt(self.cal_syx), self.cal_n), "LOD " + fmt(self.cal_lod), "LOQ " + fmt(self.cal_loq), "DF " + fmt(self.cal_dilution), "LEFT:page1"))
            elif self.page == 0:
                self.screen.show(("2PT STATUS 1/2", "Std " + fmt(self.cal_standard), "RFU " + fmt(self.cal_rfu), "Slope " + fmt(self.cal_slope), "QC " + self.cal_qc, "LOD " + fmt(self.cal_lod), "LEFT:page2"))
            else:
                self.screen.show(("2PT STATUS 2/2", "Blank " + fmt(self.blank_mean), "BlankSD " + fmt(self.blank_sd), "Limit n " + str(self.limit_n), "Limit SD " + fmt(self.limit_sd), "LOQ " + fmt(self.cal_loq), "LEFT:page1"))
        elif self.mode == "clear":
            self.screen.show(("CLEAR CALIBRATION?", "Removes active", "2-point or imported", "multipoint model.", "", "SELECT:confirm", "B:cancel"))
        elif self.mode == "mp_load":
            self.screen.show(("LOAD MULTIPOINT?", self.mp_file[:24], "Use Suite JSON", "Current sensor cfg", "will be attached.", "", "SELECT:load B:cancel"))

    def _log(self, row_type, sample_id):
        if not self.csv_logging:
            return
        header = "t_s,firmware_version,row_type,sample_id,sensor_channel,gain,integration_time_ms,full_1,full_2,full_3,ir_1,ir_2,ir_3,vis_1,vis_2,vis_3,full_mean,full_sd,ir_mean,ir_sd,vis_mean,vis_sd,blank_mean,blank_sd,rfu,calibration_enabled,calibration_type,calibration_model,calibration_status,dilution_factor,range_min_ng_uL,range_max_ng_uL,cal_intercept_rfu,cal_slope_rfu_per_ng_uL,concentration_ng_uL,concentration_in_assay_ng_uL,pi_low_ng_uL,pi_high_ng_uL,lod_ng_uL,loq_ng_uL,lod_in_assay_ng_uL,loq_in_assay_ng_uL,result_flag,qc\n"
        try:
            try:
                with open(LOG_FILE, "r"):
                    new_file = False
            except OSError:
                new_file = True
            log_blank_mean = self.cal_blank[0] if row_type.startswith("calibration") and self.cal_blank else self.blank_mean
            log_blank_sd = self.cal_blank[1] if row_type.startswith("calibration") and self.cal_blank else self.blank_sd
            values = (
                "%.1f" % time.monotonic(), VERSION, row_type, sample_id,
                self.sensor_channel, self.gain_name, self.integration_ms,
                self.full[0], self.full[1], self.full[2],
                self.ir[0], self.ir[1], self.ir[2],
                self.vis[0], self.vis[1], self.vis[2],
                self.full_mean, self.full_sd, self.ir_mean, self.ir_sd,
                self.vis_mean, self.vis_sd, log_blank_mean, log_blank_sd,
                self.rfu, self.cal_enabled, self.cal_type, self.cal_model,
                self.cal_status, self.cal_dilution, self.cal_x_min, self.cal_x_max,
                self.cal_intercept, self.candidate_slope if row_type == "calibration_standard" else self.cal_slope,
                self.concentration,
                None if self.concentration is None else self.concentration / (self.cal_dilution or 1.0),
                self.ci_low, self.ci_high,
                self.cal_lod, self.cal_loq,
                None if self.cal_lod is None else self.cal_lod / (self.cal_dilution or 1.0),
                None if self.cal_loq is None else self.cal_loq / (self.cal_dilution or 1.0),
                self.result_flag,
                self.candidate_qc if row_type == "calibration_standard" else self.cal_qc,
            )
            with open(LOG_FILE, "a") as file_obj:
                if new_file:
                    file_obj.write(header)
                for i, value in enumerate(values):
                    if i:
                        file_obj.write(",")
                    file_obj.write("" if value is None else str(value))
                file_obj.write("\n")
            self.fs_status = "CSV saved"
        except OSError as error:
            self.fs_status = "FS read-only" if error.args and error.args[0] == 30 else "CSV error"

    def _back(self):
        if self.mode in ("menu", "details", "raw"):
            self.mode = "live"
        elif self.mode in ("cal_blank", "cal_select", "cal_standard", "cal_review", "limit", "limit_result", "mp_load"):
            if self.mode in ("limit", "limit_result"):
                self._load_calibration()
            self.mode = "menu"
            self.status = "Calibration cancelled"
        elif self.mode in ("cal_status", "clear"):
            self.mode = "menu"
        self.page = 0
        self._update()

    def _select(self):
        if self.mode == "live":
            self.mode = "menu"
        elif self.mode == "menu":
            if self.menu_index == 0:
                self._start_calibration()
                return
            if self.menu_index == 1:
                self._start_limits()
                return
            if self.menu_index == 2:
                self.mode = "mp_load"
            elif self.menu_index == 3:
                self.mode = "cal_status"
                self.page = 0
            else:
                self.mode = "clear"
        elif self.mode == "cal_select":
            self.mode = "cal_standard"
            self.status = "Ready"
        elif self.mode == "cal_review":
            self._save_calibration()
            return
        elif self.mode == "limit_result":
            self._save_limits()
            return
        elif self.mode == "mp_load":
            self._import_multipoint()
            return
        elif self.mode == "clear":
            self._clear_calibration()
            return
        elif self.mode == "cal_status":
            self.mode = "menu"
        self._update()

    def _button(self, event):
        if event is None or event.pressed:
            return
        key = event.key_number
        if key == constants.BUTTON["menu"]:
            self._select()
        elif key == constants.BUTTON["gain"]:
            self._back() if self.mode not in ("live", "details", "raw") else self._cycle_view()
        elif key == constants.BUTTON["norm"]:
            if self.mode == "cal_blank":
                self._measure_cal_blank()
            elif self.mode == "limit":
                self._measure_limit_blank()
            elif self.mode in ("live", "details", "raw"):
                self.measure_blank()
        elif key == constants.BUTTON["itime"]:
            if self.mode == "cal_standard":
                self._measure_cal_standard()
            elif self.mode in ("live", "details", "raw"):
                self.measure_sample()
        elif key == constants.BUTTON["up"]:
            if self.mode == "menu":
                self.menu_index = (self.menu_index - 1) % len(MENU)
            elif self.mode == "cal_select":
                self.std_index = (self.std_index - 1) % len(self.std_values)
            elif self.mode == "live":
                self.sample_index = (self.sample_index - 1) % len(self.sample_list)
                self._save_state()
            self._update()
        elif key == constants.BUTTON["down"]:
            if self.mode == "menu":
                self.menu_index = (self.menu_index + 1) % len(MENU)
            elif self.mode == "cal_select":
                self.std_index = (self.std_index + 1) % len(self.std_values)
            elif self.mode == "live":
                self.sample_index = (self.sample_index + 1) % len(self.sample_list)
                self._save_state()
            self._update()
        elif key == constants.BUTTON["right"]:
            if self.mode in ("live", "details", "raw"):
                self.mode = "live" if self.mode == "raw" else "raw"
                self.page = 0
                self._update()
        elif self.left_key is not None and key == self.left_key:
            if self.mode in ("raw", "cal_review", "cal_status"):
                self.page = 1 - self.page
                self._update()

    def _cycle_view(self):
        self.mode = "details" if self.mode == "live" else ("raw" if self.mode == "details" else "live")
        self.page = 0
        self._update()

    def run(self):
        while True:
            self._button(self.pad.events.get())
            time.sleep(0.05)
