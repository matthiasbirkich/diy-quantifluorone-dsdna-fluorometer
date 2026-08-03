# Changelog

## QF1-1.0.0-rc2

- Corrected live-screen priority after a multipoint sample measurement.
- Recalculate the individual two-sided prediction interval immediately before logging and display.
- Show the compact half-width form `95% PI +/- ...`.
- Keep LOD and LOQ visible before the first sample and in `CAL STATUS`.
- Show `95% PI unavailable` if required prediction statistics are missing or invalid.
- Validate syx, slope, N, x-mean, Sxx and the t factor before interval calculation.
- New log file: `quantifluorone_log_v100rc2.csv`.

## QF1-1.0.0-rc1

- Added the provisional v1.0 Calibration Suite JSON import workflow.
- Included a transparent provisional multipoint calibration for software verification.
- Added explicit `PROVISIONAL` calibration status on the display and in CSV output.
- Added configured 1 µL sample + 200 µL reagent preparation and dilution factor 201.
- Changed blank-based LOD from 3σ to 3.3σ for comparison with the DIYNAFLUOR publication; LOQ remains 10σ.
- Added original-sample and in-assay LOD/LOQ metadata.
- Added original-sample and in-assay concentration output.
- Added calibration-range limits and `BELOW RANGE` / `ABOVE RANGE` warnings.
- Added calibration status, dilution factor, range, in-assay values and range flag to the v1.0 CSV.
- Clarified the startup display: `cal=PROV c=not measured` or `cal=none c=uncalibrated`.
- New log file: `quantifluorone_log_v100.csv`.
