# References and Acknowledgements

This project combines open-source hardware, commercial laboratory reagents, scientific standards and original engineering developments. The references listed below provide the scientific and technical background for the DIY-QuantiFluorONE-dsDNA-Fluorometer.

Complete bibliographic information is maintained in the repository (`references.bib`). Additional information regarding hardware provenance, upstream repositories, software versions and applicable standards is documented in the accompanying repository metadata.

---

## Scientific References

The analytical methods and performance evaluation described in this documentation are based on internationally accepted standards and the documentation supplied by the respective manufacturers.

Primary references include:

- Promega QuantiFluor® ONE dsDNA System Technical Manual
- DIN 32645 — Detection limit, decision limit and determination limit
- DIN 38402-A51 — Calibration of analytical methods
- Standard literature on fluorescence spectroscopy and analytical fluorometry

---

## Open Hardware and Software

The DIY-QuantiFluorONE-dsDNA-Fluorometer builds upon several excellent open-source projects.

### ioRodeo

- Open Colorimeter Plus
- Fixed-Current Radial LED Board (modified for rear-side LED mounting)

### DIYNAFLUOR

- Open-source optical concept
- Mechanical inspiration for the optical module

### Adafruit

- PyBadge development platform
- TSL2591 High Dynamic Range Light Sensor
- PCA9546 STEMMA QT / Qwiic I²C Multiplexer

---

## Commercial Components

Commercial products used in this project include:

- Promega QuantiFluor® ONE dsDNA System
- Neemoo optical band-pass filters
- High-brightness 485 nm excitation LED

These components are referenced solely to document the hardware configuration used during validation and workshop preparation.

---

## Engineering Contributions

The optical module is based on the open-source DIYNAFLUOR concept and was extensively redesigned and adapted for the DIY-QuantiFluorONE-dsDNA-Fluorometer.

The mechanical modifications, optimisation of the optical module and integration into the PyBadge enclosure were jointly developed by

- Dipl.-Ing. Matthias Birkicht 
- Florian Bock
  3D-Haven
  27570 Bremerhaven
  Germany

for the present project.

---

## Repository Metadata

Detailed source information is maintained in the repository:

- `references.bib`
- `hardware_sources.yml`
- `source_register.csv`
- `standards_register.md`
- `SOURCE.md` files located in the respective upstream directories

These files provide complete bibliographic information, hardware provenance, software sources and engineering traceability.

---

## Acknowledgements

The authors gratefully acknowledge the open-source community and the developers of the upstream projects whose work made this project possible.

Special thanks are extended to the developers of the ioRodeo Open Colorimeter platform, the DIYNAFLUOR project, Adafruit Industries and Promega Corporation for providing openly accessible documentation and technical resources.