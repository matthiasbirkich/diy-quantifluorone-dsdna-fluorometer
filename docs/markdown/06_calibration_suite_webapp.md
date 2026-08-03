# DIY-QuantiFluorONE-dsDNA-Fluorometer — Calibration Suite Web App

## 1. Purpose

The repository includes the current browser-based calibration utility as a local web app. The tool is stored in the repository so that workshop participants and project partners can use the same calibration environment without depending on an external server.

## 2. Repository location

The current files are stored in:

- `tools/calibration_suite/Open_Fluorometer_Calibration_Suite_v7.2_Dynamic_Axis_Labels.html`
- `tools/calibration_suite/Open_Fluorometer_Calibration_Suite_v7.2_Dynamic_Axis_Labels.txt`

## 3. Basic workflow

1. Open the HTML file in a current desktop browser.
2. Load or paste the calibration data required by the app.
3. Review the plotted data and the resulting calibration output.
4. Record the calibration parameters required for the fluorometer workflow.
5. Store calibration exports together with the experimental metadata whenever possible.

## 4. Recommended repository practice

- keep the web app under version control;
- record the active calibration-suite version in documentation and workshop notes;
- store example calibration data separately from the app itself;
- treat the web app as a reproducibility tool, not merely as a convenience file.

## 5. Booklet integration

This chapter can be included as an appendix in the workshop booklet or replaced later by a more detailed software and calibration chapter.


## 6. Compatibility note for QF1-1.0.0-rc2

The supplied Calibration Suite v7.2 Stable displays a firmware target of `v8.2+` and includes a function that updates a `configuration.json` file containing a `diynafluor` section. QuantiFluorONE `QF1-1.0.0-rc2` uses a different file layout:

- `quantifluorone_config.json` for device settings;
- `quantifluorone_multipoint.json` for the model imported through `SELECT → LOAD MP CAL`.

Therefore, do **not** replace the RC2 configuration with a suite-generated `configuration.json`. A dedicated RC2 export adapter or a compatible `quantifluorone_multipoint.json` export is required before direct transfer from the suite to RC2.
