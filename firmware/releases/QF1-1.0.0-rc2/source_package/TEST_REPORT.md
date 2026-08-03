# QF1-1.0.0-rc1 Test Report

The following checks were completed before packaging:

- Python syntax compilation for `boot.py`, `code.py` and `quantifluorone_app.py`;
- JSON syntax validation for the configuration, provisional calibration and schema example;
- simulated direct-TSL2591 startup;
- import and normalization of `quantifluorone_multipoint.json`;
- persistence to `quantifluorone_calibration.json`;
- reload of the calibration after a simulated restart;
- persistent reagent-blank storage and reload;
- concentration prediction at an exact simulated 250 ng/µL target;
- two-sided prediction-interval calculation;
- `ABOVE RANGE` warning at a simulated 800 ng/µL result;
- CSV output with 44 header fields and 44 values per data row;
- confirmation that the provisional status and dilution factor 201 survive restart.

The hardware-specific test still required is operation on the actual PyBadge, PCA9546A and TSL2591 assembly.
