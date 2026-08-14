---
document-status: "Current"
validation-status: "Validated configuration"
date: "2026-08-14"
---

> **Firmware basis:** QuantiFluorONE `QF1-1.0.0-rc2`, display version `v1.0 RC2`.

## Front-panel controls

![QuantiFluorONE front-panel controls for firmware QF1-1.0.0-rc2.](../figures/qfo_getting_started_menu_navigation.jpeg)

The firmware defines the controls as follows:

| Physical control | Firmware name | Main measurement-screen function | Menu or dialog function |
|---|---|---|---|
| Upper-left button | `SELECT` | Open the SELECT menu | Open, confirm, load, or save the highlighted action |
| Upper-right button | `START` | Measure and store the reagent blank | Measure a calibration blank or the next blank in the ten-blank study |
| A button | `A` | Measure the selected sample; one cycle contains three sensor readings | Measure the selected high standard during two-point calibration |
| B button | `B` | Cycle Live → Details → RAW → Live | Back or cancel |
| D-pad UP/DOWN | `UP/DOWN` | Select the sample ID | Select a menu item or standard concentration |
| D-pad RIGHT | `RIGHT` | Open or leave the RAW screen | Not used for menu selection |
| D-pad LEFT | `LEFT` | Change RAW page | Change calibration-result or calibration-status page |
| On/Off switch | power | Turn the instrument on or off | — |
| Reset access opening | reset | Restart the PyBadge | Used for normal reset, slow-double-click safe mode, or fast-double-click UF2 bootloader mode |
| USB Micro port | USB | Power, charging, programming, and file access | — |

The last line of the display shows context-sensitive button hints. These hints take priority whenever a calibration or confirmation dialog is open.

## Preparing and documenting the sample list

Before starting a measurement series, the sample identifiers can be entered in `quantifluorone_config.json`. This is recommended because the selected sample ID is written to the measurement CSV file and allows each measurement to be assigned directly to the corresponding laboratory sample.

Editing the sample list is optional. If the list is not updated, the exact order in which the physical samples are measured must be recorded separately in the laboratory notebook. Without such a record, measurements in the CSV file may no longer be assignable reliably to the original samples after the measurement series.

### Editing the sample list

1. Connect the switched-on fluorometer to the computer using a USB data cable.

2. Enter CircuitPython safe mode using the **slow double-click** of the Reset button:
   - press Reset once;
   - allow the restart sequence to begin; and
   - press Reset a second time during the approximately one-second startup window.

3. Confirm that the `CIRCUITPY` drive is available on the computer.

4. Open `quantifluorone_config.json` with a plain-text editor.

   Suitable examples are:
   - Windows Notepad;
   - Notepad++;
   - Visual Studio Code; or
   - another editor that saves plain-text files without changing the JSON structure.

   Do not edit the file with a word processor such as Microsoft Word.

5. Locate the `samples` section and enter the required sample identifiers, for example:

```json
"samples": {
  "list": ["Blank", "Std400", "QC1", "Sample01", "Sample02"],
  "selected_index": 0
}
```

Use short, unique identifiers because the display width is limited. The complete identifier is retained in the measurement data even when only part of it is visible on the instrument display.

6. Save `quantifluorone_config.json` without changing its filename or file type.

7. Safely eject the `CIRCUITPY` drive from the computer.

8. Disconnect the USB data connection.

9. Connect the fluorometer to its normal standalone power source, such as a power bank, and restart it normally.

10. Use **UP/DOWN** on the measurement screen to select the required sample ID before measuring the corresponding sample with **A**.

### If the sample list is not edited

Updating `quantifluorone_config.json` is not mandatory. The instrument can also be used with the existing sample list.

In this case, record the physical samples and their measurement order explicitly in the laboratory notebook, for example:

```text
Measurement 1  = Sample A17
Measurement 2  = Sample A18
Measurement 3  = Sample B03
Measurement 4  = Sample B04
```

**Important:** The CSV file records the sample identifier selected on the instrument. If this identifier does not correspond to the actual sample and no separate measurement-order record is kept, the analytical result may not be assignable reliably to the original sample afterwards.

Whenever practical, prepare the sample list before the measurement series and keep the displayed sample order consistent with the physical order of the prepared tubes.

## Normal measurement workflow

1. Switch the instrument on and wait for `QuantiFluorONE v1.0 RC2`.
2. Use D-pad UP or DOWN to select the required sample ID.
3. Insert a fresh reagent blank and close the light shield.
4. Press START. The instrument performs three TSL2591 readings and stores the blank mean and standard deviation.
5. Replace the blank with the prepared sample and close the light shield.
6. Press A. The instrument performs one sample cycle of three sensor readings.
7. Read concentration, prediction interval, VIS, standard deviation, blank, and RFU from the live screen.
8. Press B for the details screen or RIGHT for raw readings.

## SELECT menu

Press SELECT from the live screen to open:

```text
SELECT MENU
>2-PT CAL
 10-BLANK L/Q
 LOAD MP CAL
 CAL STATUS
 CLEAR CAL
```

Use UP/DOWN to move the selection, SELECT to open or confirm, and B to return or cancel.

## Display views

### Live

The live screen displays the sample ID, concentration or calibration status, prediction interval or LOD/LOQ, VIS mean and SD, blank, and RFU.

### Details

Press B from Live. The details screen shows FULL, IR, VIS, RFU, concentration, sensor channel, gain, and integration time.

### RAW

Press B again, or press RIGHT from Live/Details. LEFT changes between the two raw-data pages. RIGHT returns to Live.

## Multipoint calibration import

1. Place the compatible `quantifluorone_multipoint.json` file in the root of `CIRCUITPY`.
2. Disconnect the USB data host and power the device from a charger or power bank so the firmware can write its state files.
3. Press SELECT.
4. Choose `LOAD MP CAL`.
5. Confirm with SELECT.
6. Measure a fresh reagent blank with START before measuring samples.

The multipoint calibration used for quantitative measurements must correspond to the validated calibration workflow described in this repository. Verify the calibration identity, working range, concentration basis, and status before measuring samples.

## Managing CSV and JSON files: use the slow double-click

> **Important — slow double-click required:** Before copying, replacing, deleting, or downloading CSV, JSON, or firmware files, enter CircuitPython **safe mode** with a slow double-click of the Reset button. Press Reset once, then press it again during the approximately one-second startup window. The display reports that code has stopped and will not run the saved application.

In safe mode:

- `CIRCUITPY` remains available to the computer;
- the QuantiFluorONE application does not run;
- automatic reload is disabled;
- files can be copied, downloaded, replaced, or deleted without the firmware actively using them.

A **fast** double-click is different: it opens `PYBADGEBOOT` or `BADGEBOOT` and is used only for UF2 installation.

## Files produced or used by RC2

| File | Purpose |
|---|---|
| `quantifluorone_log_v100rc2.csv` | Measurement log |
| `quantifluorone_state.json` | Blank and interface state |
| `quantifluorone_calibration.json` | Active saved calibration |
| `quantifluorone_multipoint.json` | Multipoint model imported through `LOAD MP CAL` |
| `quantifluorone_config.json` | Hardware, measurement, sample, assay, and calibration settings |

Always back up required data and safely eject the drive before resetting, switching off, or disconnecting USB.


---

⬅️ Previous Chapter: [Software Installation](05_software_installation.md)

📖 [Documentation Summary](SUMMARY.md)

➡️ Next Chapter: [Calibration Suite and Data Transfer](07_calibration_suite_and_data_transfer.md)
