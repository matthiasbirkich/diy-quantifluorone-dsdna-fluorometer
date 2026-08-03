# QuantiFluorONE device firmware

## Current supported release

```text
QuantiFluorONE_Firmware_1.0.0-rc2-stable.zip
```

This archive is preserved unchanged as the tested firmware release for the
current instrument build. Do not replace it with a shortened, cleaned, or
repacked derivative.

## Clean installation

1. Back up the complete existing `CIRCUITPY` drive.
2. Enter CircuitPython safe mode with the slow reset double-click.
3. Delete the complete contents of `CIRCUITPY`.
4. Extract the stable RC2 ZIP on the computer.
5. Open the extracted `QuantiFluorONE_Firmware_1.0.0-rc2-stable` folder.
6. Copy all files and folders **inside** that folder to the root of the empty
   `CIRCUITPY` drive.
7. Do not copy the enclosing release folder itself.
8. Safely eject and restart the device.
9. Confirm `QuantiFluorONE v1.0 RC2` on the display.

The included calibration remains marked `PROVISIONAL`; the stable designation
refers to the tested software package and operating workflow, not to completed
analytical-method validation.
