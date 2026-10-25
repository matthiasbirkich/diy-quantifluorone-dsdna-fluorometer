# Open Fluorometer Calibration Suite

[Launch v7.3 in the browser](https://matthiasbirkich.github.io/diy-quantifluorone-dsdna-fluorometer/software/calibration_suite/Open_Fluorometer_Calibration_Suite_v7.3.html). See Chapter 8 of the [manual](../../docs/manual/README.md) for operating instructions.

The repository includes v7.2 Dynamic Axis Labels and v7.3 Standards-Audit HTML applications and their text sources. Open the HTML locally in a desktop browser; retain the selected version and its report with each calibration.

## Device compatibility

The on-device two-point workflow is documented in the new manual. The suites can evaluate multipoint data, but their exports must be checked against the target firmware.

- v7.3 scientific JSON is not directly accepted by the preserved QuantiFluorONE RC2 importer: model labels and mathematical field names differ.
- v7.2 scientific JSON is closer to the RC2 mathematical contract but omits dilution/range/status metadata required for the intended operational record. Its separate DIYNAFLUOR configuration export targets another application.
- Do not rename an arbitrary suite export and assume it is ready for `LOAD MP CAL`. The verified export/conversion workflow is tracked as SW-02.
- Never use the bundled provisional example as the calibration of a newly built instrument.

See [calibration management](../../docs/manual/chapters/08_calibration.qmd) and [the v7.3 audit notes](V7.3_STANDARDS_AUDIT_NOTES.md) for the documented scope. The firmware archive remains unchanged.
