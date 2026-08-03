# QuantiFluorONE Firmware QF1-1.0.0-rc2

## Status

This package is a **provisional v1.0 release candidate** for software and hardware testing.

It is not yet a validated analytical-method release. The included multipoint calibration was derived from aged standards whose apparent concentrations were obtained from the earlier two-point calibration. It is intentionally marked `PROVISIONAL` and must later be replaced by a Calibration Suite export based on freshly prepared standards and independent reference measurements.

## Main v1.0 functions

- one TSL2591 sensor on a PCA9546A multiplexer;
- automatic sensor-channel detection;
- three sensor readings per measurement cycle;
- FULL, IR and VIS raw screens;
- reagent-blank storage;
- two-point calibration;
- ten-blank LOD/LOQ study;
- import of an OLS multipoint JSON file from the Calibration Suite;
- inverse concentration prediction;
- two-sided prediction interval for one analytical determination;
- calibration-range warnings;
- explicit `PROVISIONAL` calibration status;
- original-sample and in-assay concentration metadata;
- CSV logging with raw readings, calibration metadata, prediction limits and LOD/LOQ;
- splash screen at startup.

## Required base installation

Start from a working installation of:

```text
open_colorimeter_plus_firmware_v0.1.1
```

Keep the original:

```text
/src/constants.py
/lib
/splashscreen.bmp
/images and/or /assets
```

The firmware adds `/src` to the Python import path automatically. Do not move `constants.py` to the root directory.

## Installation

Copy these files to the root of `CIRCUITPY`, replacing previous QuantiFluorONE versions:

```text
boot.py
code.py
quantifluorone_app.py
quantifluorone_config.json
quantifluorone_multipoint.json
```

Remove this obsolete file if it is still present:

```text
quantifluorone_math.py
```

The included `quantifluorone_multipoint.json` is the provisional software-test calibration.

## Important filesystem behaviour

When the PyBadge is connected to a USB data host, `CIRCUITPY` remains writable by the computer and read-only to the firmware. Calibration, blank state and CSV files can be saved by the firmware when the device is powered from a charger or power bank.

Recommended import sequence:

1. Copy the firmware and JSON file while connected to the computer.
2. Safely disconnect the drive.
3. Power the PyBadge from a charger or power bank.
4. Press `SELECT` and choose `LOAD MP CAL`.
5. Confirm the import.
6. Measure a fresh reagent blank with `START`.
7. Measure samples with `A`.

## Controls

| Control | Function |
|---|---|
| A | Measure sample: one cycle of three sensor readings |
| START | Measure and store reagent blank |
| B | Live → Details → RAW → Live; back/cancel in menus |
| RIGHT | Open or leave RAW screen |
| LEFT | Change RAW, calibration-result or calibration-status page |
| UP/DOWN | Select sample ID or menu item |
| SELECT | Open menu or confirm an action |

## SELECT menu

```text
SELECT MENU
>2-PT CAL
 10-BLANK L/Q
 LOAD MP CAL
 CAL STATUS
 CLEAR CAL
```

## Assay preparation and concentration basis

The configured preparation is:

```text
1 µL sample + 200 µL QuantiFluor ONE reagent = 201 µL total
```

The dilution factor is therefore:

```text
201
```

Firmware concentrations are reported on the **original-sample basis**. The CSV also includes the corresponding in-assay concentration.

## Multipoint calculation

The imported regression is defined as:

```text
RFU = intercept + slope × concentration
```

where:

```text
RFU = VISsample − VISblank
```

The estimated original-sample concentration is:

```text
xhat = (RFU − intercept) / slope
```

For one analytical determination, the prediction standard error is:

```text
sx = syx / |slope| × sqrt(
    1
    + 1 / N
    + (xhat − xmean)^2 / Sxx
)
```

The two-sided prediction interval is:

```text
xhat ± t × sx
```

The three TSL2591 readings are technical sensor repeats used to calculate one measurement-cycle mean and SD. They are not treated as three independently prepared unknown samples.

## Calibration range warning

The imported JSON defines `range_min_ng_uL` and `range_max_ng_uL`.

A result outside that range is marked:

```text
BELOW RANGE
```

or:

```text
ABOVE RANGE
```

The numerical value is retained in the CSV for diagnostic purposes but should not be reported as a routine validated quantitative result.

## LOD and LOQ

The firmware and included provisional JSON use the blank-based approach applied in the DIYNAFLUOR publication:

```text
LOD = 3.3 × blank SD / slope
LOQ = 10 × blank SD / slope
```

The ten blank-cycle means are used to calculate the blank SD. Each cycle contains three TSL2591 readings.

For the included provisional dataset:

```text
LOD, original sample: 7.874 ng/µL
LOQ, original sample: 23.862 ng/µL
LOD, in assay:        0.03918 ng/µL
LOQ, in assay:        0.11871 ng/µL
```

These are empirical software-test estimates, not a completed formal method validation.

## Provisional calibration included in this package

The included JSON uses these apparent original-sample concentration levels:

```text
0, 5.5, 10, 75, 250, 375 and 670 ng/µL
```

The zero level is the mean of ten v0.60 blank cycles. Each positive level is the mean of two measurement cycles.

The descriptive regression is:

```text
RFU = 332.5952 + 53.01984 × concentration
R² = 0.999861
residual SD = 173.063 RFU
N = 7 concentration-level means
```

Important limitations:

- the assigned concentrations were derived from the earlier two-point calibration;
- they are not independent certified or reference-instrument values;
- standards were more than one week old;
- five of six positive levels showed a lower second reading, consistent with photobleaching or time drift;
- the pipette and tips used for preparation were later found to be unreliable;
- the excitation LED was not yet mechanically rigid.

The high R² must therefore not be presented as independent validation of linearity.

## Display interpretation

Before the first sample measurement with the included JSON:

```text
cal=PROV c=not measured
```

After a multipoint measurement:

```text
c=... ng/uL PROV
95% PI +/- ...
```

The second line is the two-sided prediction-interval half-width for one analytical
determination. LOD and LOQ are shown before a sample has been measured and remain
available under `SELECT → CAL STATUS`. They are not used as a substitute for an
individual prediction interval after a multipoint sample measurement.

If required prediction-statistics fields are absent or invalid, the display states:

```text
95% PI unavailable
```

instead of silently falling back to LOD and LOQ.

`PROV` means that the active model is provisional and intended for software verification.

## Files created by the firmware

```text
/quantifluorone_state.json
/quantifluorone_calibration.json
/quantifluorone_log_v100rc2.csv
```

The imported suite JSON remains:

```text
/quantifluorone_multipoint.json
```

## CSV additions in v1.0 RC2

The log contains 44 columns, including:

- all three FULL, IR and VIS readings;
- means and sample SD values;
- current blank and RFU;
- calibration type, model and status;
- dilution factor;
- accepted calibration range;
- intercept and slope;
- original-sample concentration;
- in-assay concentration;
- prediction interval;
- original-sample LOD and LOQ;
- in-assay LOD and LOQ;
- range flag and QC field.

## Replacing the provisional calibration later

The final validation JSON should be generated from:

- freshly prepared standards;
- a verified pipette and compatible tips;
- a mechanically fixed excitation LED;
- consistent tube type and orientation;
- blank and standards measured in the same session;
- independent reference concentrations from the commercial QuantiFluor instrument;
- documented calibration-model diagnostics in the Calibration Suite.

Export the accepted OLS model from the Calibration Suite as `quantifluorone_multipoint.json`, copy it to `CIRCUITPY`, and use `SELECT → LOAD MP CAL` again.

## Included supporting files

```text
PROVISIONAL_SOURCE_DATA.csv
PROVISIONAL_CALIBRATION_NOTES.md
CALIBRATION_SUITE_JSON_EXAMPLE.json
CHANGELOG.md
INSTALL.txt
```


## RC2 prediction-interval display correction

RC1 could display LOD and LOQ after a multipoint sample measurement even though the
individual prediction interval should have had display priority. RC2 recalculates the
interval immediately before logging and display, validates all imported statistics, and
shows the compact half-width form:

```text
95% PI +/- 10.9
```

The lower and upper limits continue to be stored separately in the CSV columns
`pi_low_ng_uL` and `pi_high_ng_uL`.
