# Software

This directory contains the three software components required for the current
DIY-QuantiFluorONE-dsDNA-Fluorometer build:

```text
software/
├── bootloader/                   PyBadge UF2 bootloader files
├── circuitpython/                CircuitPython runtime
└── quantifluorone_firmware/      one supported device-firmware release
```

## Supported versions

- PyBadge bootloader: 3.15.0
- CircuitPython: 9.1.1
- QuantiFluorONE device firmware: QF1-1.0.0-rc2 stable

The main repository intentionally presents one current QuantiFluorONE firmware
release. Earlier development versions remain traceable through Git history,
tags, or GitHub releases rather than as parallel installation choices in this
directory.

Installation order:

1. update the bootloader only when required;
2. install CircuitPython 9.1.1 when required;
3. back up and empty `CIRCUITPY`;
4. copy the complete contents of the extracted stable RC2 release to the root of
   `CIRCUITPY`.

See `docs/markdown/07_software_installation.md`.
