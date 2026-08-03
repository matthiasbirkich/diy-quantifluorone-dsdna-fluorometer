# PyBadge UF2 bootloader 3.15.0

Included files:

- `update-bootloader-arcade_pybadge-v3.15.0.uf2`
- `bootloader-arcade_pybadge-v3.15.0.bin`

## Recommended workshop update file

Use the UF2 updater for the normal USB drag-and-drop workflow:

`update-bootloader-arcade_pybadge-v3.15.0.uf2`

1. Connect the PyBadge using a USB Micro data cable.
2. Enter the UF2 bootloader with a **fast double-click** of Reset.
3. Wait for `PYBADGEBOOT` or `BADGEBOOT` to appear.
4. Copy `update-bootloader-arcade_pybadge-v3.15.0.uf2` to that drive.
5. Wait for the board to restart.
6. Re-enter UF2 bootloader mode and verify version 3.15.0 in `INFO_UF2.TXT`.
7. Reinstall CircuitPython 9.1.1 afterwards.

## Raw binary archive

`bootloader-arcade_pybadge-v3.15.0.bin` is retained for open-science archiving
and technical recovery. **Do not copy this `.bin` file directly to
`PYBADGEBOOT` or `BADGEBOOT`.** It is not the normal workshop installation file.
