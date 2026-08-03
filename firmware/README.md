# QuantiFluorONE firmware

This directory stores the supplied QuantiFluorONE firmware release and a curated
CIRCUITPY installation payload.

## Release

- firmware version: `QF1-1.0.0-rc2`
- display version: `v1.0 RC2`
- target board: Adafruit PyBadge, Product ID 4200
- tested CircuitPython image supplied in this repository: `9.1.1`

## Directory layout

- `releases/archives/` — original release ZIP as supplied
- `releases/QF1-1.0.0-rc2/source_package/` — original release extracted without source edits
- `device_install/QF1-1.0.0-rc2_CIRCUITPY/` — curated runtime files
- `device_install/QuantiFluorONE_QF1-1.0.0-rc2_CIRCUITPY.zip` — copy the **contents** of this ZIP to `CIRCUITPY`

The device-install payload intentionally excludes generated logs, state files,
calibration-state files, desktop test files, `__pycache__`, and release notes.

## Important

Enter CircuitPython safe mode using the **slow double-click** before deleting,
copying, replacing, or downloading files on `CIRCUITPY`. The fast double-click
opens the UF2 bootloader drive and is used only for UF2 installation.
