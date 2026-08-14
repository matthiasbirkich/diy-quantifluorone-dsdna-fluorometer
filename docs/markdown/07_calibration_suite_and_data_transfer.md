---
document-status: "Current"
validation-status: "Validated configuration"
date: "2026-08-14"
---

## Purpose

The repository includes the current browser-based Calibration Suite as a local web app. This chapter covers the calibration workflow and the safe transfer of compatible calibration files to the QuantiFluorONE firmware.

## Repository location

The current files are stored in:

- `tools/calibration_suite/Open_Fluorometer_Calibration_Suite_v7.3.html`
- `tools/calibration_suite/Open_Fluorometer_Calibration_Suite_v7.3.txt`

## Basic workflow

1. Open the HTML file in a current desktop browser.
2. Load or paste the calibration data required by the app.
3. Review the plotted data and the resulting calibration output.
4. Record the calibration parameters required for the fluorometer workflow.
5. Store calibration exports together with the experimental metadata whenever possible.

## Recommended repository practice

- keep the web app under version control;
- record the active calibration-suite version in documentation and workshop notes;
- store example calibration data separately from the app itself;
- treat the web app as a reproducibility tool, not merely as a convenience file.

## Calibration-file transfer

1. Export and retain the complete calibration report and source data.
2. Transfer only a file that is explicitly compatible with QuantiFluorONE `QF1-1.0.0-rc2`.
3. Enter CircuitPython safe mode with the slow double-click before replacing JSON files on `CIRCUITPY`.
4. Back up the existing JSON file before replacement.
5. Safely eject `CIRCUITPY`, restart normally, and confirm the calibration status on the instrument.


---

⬅️ Previous Chapter: [Getting Started – Basic Operation and Menu Navigation](06_getting_started_basic_operation_and_menu_navigation.md)

📖 [Documentation Summary](SUMMARY.md)

➡️ Next Chapter: [Measurement Protocol](08_measurement_protocol.md)
