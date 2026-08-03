# DIY-QuantiFluorONE-dsDNA-Fluorometer — push overlay v5

Merge this overlay into the repository root. The ZIP contains repository paths
directly and has no additional outer wrapper directory.

## Main additions carried forward

- firmware release `QF1-1.0.0-rc2` and curated device installer
- CircuitPython 9.1.1 UF2
- exact firmware-derived control map and annotated real-device figure
- software installation chapter in Markdown and Quarto form
- slow-double-click safe-mode procedure for firmware, CSV, and JSON file management
- confirmed M2.5 x 20 and M3 x 20 fasteners and matching nuts
- Quarto booklet structure and installation chapter

## New in v5

The correct drag-and-drop PyBadge bootloader updater is now included:

`software/bootloader/3.15.0/update-bootloader-arcade_pybadge-v3.15.0.uf2`

The raw `.bin` file remains available for archiving and technical recovery, but
must not be copied to the UF2 boot drive during the normal workshop procedure.

## Important reset distinction

- slow double-click: CircuitPython safe mode; use for firmware, CSV, and JSON file operations
- fast double-click: UF2 bootloader drive; use for the bootloader-updater UF2 or CircuitPython UF2

## Still pending

- final PCR-tube-holder and light-shield CAD archive
- final internal wiring photographs and channel/cable map
- final cable-retention details and LiPo BOM status
