# References and Acknowledgements

This project combines open-source hardware, commercial laboratory reagents, scientific standards, manufacturer documentation and original engineering developments. This chapter records the principal sources and acknowledges the contributions on which the DIY-QuantiFluorONE-dsDNA-Fluorometer is based.

The complete machine-readable bibliography is maintained in [`docs/references/references.bib`](../references/references.bib). Additional provenance information is available in [`hardware_sources.yml`](../references/hardware_sources.yml), [`source_register.csv`](../references/source_register.csv) and [`standards_register.md`](../references/standards_register.md).

---

## Scientific and Analytical References

The theoretical and analytical framework used in this documentation is based primarily on:

- Lakowicz, J. R. *Principles of Fluorescence Spectroscopy*. 3rd ed. Springer, 2006.
- Valeur, B., and Berberan-Santos, M. N. *Molecular Fluorescence: Principles and Applications*. 2nd ed. Wiley-VCH, 2012.
- Singer, V. L., Jones, L. J., Yue, S. T., and Haugland, R. P. “Characterization of PicoGreen Reagent and Development of a Fluorescence-Based Solution Assay for Double-Stranded DNA Quantitation.” *Analytical Biochemistry* 249(2), 228–238, 1997.
- Promega Corporation. *QuantiFluor® ONE dsDNA System Technical Manual*, TM405.
- Promega Corporation. *Quantus™ Fluorometer Operating Manual*, TM396.
- DIN 38402-51:2017-05. *Calibration of analytical methods — Linear calibration (A 51)*.
- DIN 32645:2008-11. *Decision limit, detection limit and determination limit under repeatability conditions*.

The standards are cited as methodological references. Formal conformity assessment requires access to licensed copies and a documented comparison between the implemented calculations and the normative text.

---

## Open Hardware and Software Sources

The project builds upon the following open-source resources:

### ioRodeo

- Open Colorimeter Plus firmware and hardware concepts.
- Fixed-current radial 16 mA LED board, revision `ver_0p1_rev_3`.

The LED board used in this project is based on the ioRodeo design. For integration into the optical module, the through-hole LED is mounted on the rear side of the board. The board design files, licence and source record are retained in the repository for traceability.

### DIYNAFLUOR

- Published DIYNAFLUOR fluorometer concept.
- Repository containing code, bill of materials, build instructions and 3D-print files.

The optical module of the present instrument is derived from the DIYNAFLUOR concept and was modified for the installed LED board, filters, sensor geometry and PyBadge enclosure.

### Adafruit and CircuitPython

- Adafruit PyBadge, Product ID 4200.
- Adafruit TSL2591 STEMMA QT light sensor, Product ID 1980.
- Adafruit PCA9546 four-channel I²C multiplexer, Product ID 5664.
- CircuitPython for the Adafruit PyBadge. Version 9.1.1

### Spectral Verification

The project-specific filter measurements were acquired using a DIY spectrometer based on Leslie Wright’s PySpectrometer2 project. The recorded curves were normalized to their respective maxima and are used to verify spectral position and band shape rather than absolute transmittance.

---

## Commercial Components and Manufacturer Information

Commercial components are identified to document the validated hardware and assay configuration:

- Promega QuantiFluor® ONE dsDNA System.
- Promega 0.5 mL thin-walled PCR tubes.
- Neemoo Ex470BP-40 and Em532BP-40 optical band-pass filters.
- 485 nm high-brightness radial excitation LED.

Product names and supplier references are provided for reproducibility and do not imply endorsement.

---

## Engineering Contributions

The optical module is derived from the open-source DIYNAFLUOR design and was extensively adapted for the DIY-QuantiFluorONE-dsDNA-Fluorometer.

The modified 3D-print parts and their mechanical integration were jointly developed by:

- Dipl.-Ing. Matthias Birkicht, project author; and
- Florian Bock, 3D-Haven, 27570 Bremerhaven, Germany.

This work included adaptation of the optical parts, integration of the installed filters and sensor, accommodation of the rear-mounted LED board, and mechanical integration with the PyBadge enclosure.

---

## Repository Source Records

Detailed source and provenance records are maintained in:

- `docs/references/references.bib`
- `docs/references/hardware_sources.yml`
- `docs/references/source_register.csv`
- `docs/references/standards_register.md`
- component-specific `README.md` and licence files under `hardware/pcb/`

These records should be updated whenever a source, component revision, software version or standard reference changes.

---

## Acknowledgements

The project gratefully acknowledges the developers and contributors of ioRodeo Open Colorimeter, DIYNAFLUOR, Adafruit CircuitPython and PySpectrometer2, as well as the manufacturers and standards organisations whose documentation supported the development and validation of the instrument.

Special thanks are extended to Florian Bock of 3D-Haven for the collaborative development and adaptation of the mechanical parts.
