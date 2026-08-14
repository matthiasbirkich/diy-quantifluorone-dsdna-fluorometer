---
document-status: "Current"
validation-status: "Validated configuration"
date: "2026-08-14"
---

This project combines open-source hardware, commercial laboratory reagents, scientific standards, manufacturer documentation and original engineering developments. This chapter records the principal sources and acknowledges the contributions on which the DIY-QuantiFluorONE-dsDNA-Fluorometer is based.

The complete machine-readable bibliography is maintained in `references/references.bib`. Additional provenance information is available in `hardware_sources.yml`, `source_register.csv` and `standards_register.md`.

## Scientific and Analytical References

The theoretical background is based on standard works on fluorescence spectroscopy [@lakowicz2006; @valeur2012] and on published fluorescence-based dsDNA quantification methods [@singer1997].

The assay procedure and commercial reference instrument are documented by Promega [@promega_tm405; @promega_tm396].

The calibration and detection-limit framework refers to DIN 38402-51 and DIN 32645 [@din38402_51; @din32645].

The standards are cited as methodological references. Formal conformity assessment requires access to licensed copies and a documented comparison between the implemented calculations and the normative text.

## Open Hardware and Software Sources

### ioRodeo

### ioRodeo Open Colorimeter Plus and related instrumentation

The firmware and hardware concepts are derived in part from the ioRodeo Open Colorimeter Plus project [@iorodeo_ocp_firmware].

The installed LED driver is the ioRodeo fixed-current radial 16 mA LED board, revision `ver_0p1_rev_3` [@iorodeo_led_board]. For integration into the optical module, the through-hole LED is mounted on the rear side of the board. The board design files, licence, and source record are retained in the repository for traceability.

ioRodeo has also documented open photometric and fluorometric approaches to DNA quantification. The UV Open Colorimeter was used for UV-photometric dsDNA determination [@iorodeo_uv_dna_quantification], while the Open Colorimeter Plus was evaluated for fluorometric dsDNA quantification with the AccuGreen assay [@iorodeo_ocp_dna_quantitation]. Subsequent Open Colorimeter Plus hardware and firmware developments, including the dual-sensor architecture, are documented separately [@iorodeo_ocp_updates_2025].

These sources provide useful technical context for the open measurement-chain concept used in this project without being reproduced in detail in the workshop chapters.

### ioRodeo Fluorometer Tube Holder

The mechanical development of the optical sample holder also draws on the
open ioRodeo fluorometer tube-holder project:

https://github.com/iorodeo/fluorometer_tube_holder

The repository provides FreeCAD design files for the fluorometer tube holder
and is distributed under the Creative Commons Attribution 4.0 International
(CC BY 4.0) licence.

The DIY-QuantiFluorONE holder was adapted for the Promega E4941 thin-walled
0.5 mL PCR tube, the installed 8 × 8 × 1 mm optical filters, one TSL2591
sensor, and the project-specific 90° optical geometry. The resulting holder
combines design concepts from DIYNAFLUOR and ioRodeo.

The ioRodeo tube-holder and Open Colorimeter platform also illustrate how
related modular optical arrangements can be used for photometric, turbidimetric and
fluorometric measurements.

A UV-photometric approach to dsDNA determination using the UV Open Colorimeter
is described here:

https://blog.iorodeo.com/uv-dna-quantification/

A fluorometric dsDNA determination using AccuGreen and the Open Colorimeter
Plus is described here:

https://blog.iorodeo.com/open-colorimeter-plus-dna-quantitation/

In this fluorometric configuration, two TSL2591 sensors are used. The later
ioRodeo hardware description documents the detector arrangement as a 180°
geometry. This differs from the DIY-QuantiFluorONE configuration, which uses
one TSL2591 detector fixed at 90° to the excitation axis.

Later firmware and hardware developments of the Open Colorimeter Plus,
including changes relevant to this optical configuration, are described here:

https://blog.iorodeo.com/open-colorimeter-plus-firmware-and-hardware-updates/

### DIYNAFLUOR

The optical module is derived from the published DIYNAFLUOR fluorometer concept and its open repository [@anderson_diynafluor; @traulab_diynafluor]. It was modified for the installed LED board, filters, sensor geometry and PyBadge enclosure.

### Adafruit and CircuitPython

The controller and detector architecture uses the Adafruit PyBadge, TSL2591
sensor and PCA9546 multiplexer [@adafruit_pybadge; @adafruit_tsl2591;
@adafruit_pca9546]. The documented firmware environment uses CircuitPython
9.1.1 [@circuitpython_9_1_1].

### Spectral Verification

The project-specific filter measurements were acquired using a DIY spectrometer based on PySpectrometer2 [@wright_pyspectrometer2]. The recorded curves were normalized to their respective maxima and are used to verify spectral position and band shape rather than absolute transmittance.

## Commercial Components and Manufacturer Information

The validated configuration uses the Promega QuantiFluor® ONE dsDNA System [@promega_tm405], Neemoo Ex470BP-40 and Em532BP-40 band-pass filters [@neemoo_filters], and a 485 nm high-brightness radial excitation LED.

Product names and supplier references are provided for reproducibility and do not imply endorsement.

## Engineering Contributions

The optical module is derived from the open-source DIYNAFLUOR design and was extensively adapted for the DIY-QuantiFluorONE-dsDNA-Fluorometer.

The modified 3D-print parts and their mechanical integration were developed collaboratively by:

- Dipl.-Ing. Matthias Birkicht, project author; and
- Florian Bock, 3D-Haven, 27570 Bremerhaven, Germany.

This work included adaptation of the optical parts, integration of the installed filters and sensor, accommodation of the rear-mounted LED board, and mechanical integration with the PyBadge enclosure.

## Repository Source Records

Detailed source and provenance records are maintained in:

- `references/references.bib`
- `references/hardware_sources.yml`
- `references/source_register.csv`
- `references/standards_register.md`

These records should be updated whenever a source, component revision, software version or standard reference changes.

## Acknowledgements

The project gratefully acknowledges the developers and contributors of the ioRodeo Open Colorimeter Plus, DIYNAFLUOR, Adafruit CircuitPython, and PySpectrometer2 projects, as well as the manufacturers and standards organisations whose documentation supported the development and validation of the instrument.

Special thanks to Joanne Long of ioRodeo, who kindly donated a fluorometric cuvette holder for 0.2 mL tubes so that we could test the ioRodeo Colorimeter Plus for fluorometric measurements.

Special thanks are extended to Florian Bock of 3D-Haven for the collaborative development and adaptation of the mechanical parts.

The DIY-QuantiFluorONE-dsDNA-Fluorometer and this workshop documentation were prepared in the context of the 2026 eDNA workshop with Dr. Achim Meyer within the STABLE Project (2025–2027), *Higher Education Partnership for a Sustainable Blue Economy*.

## Bibliography

1. Lakowicz, J. R. (2006). *Principles of Fluorescence Spectroscopy*, 3rd ed.
   Springer. DOI: 10.1007/978-0-387-46312-4.

2. Valeur, B. & Berberan-Santos, M. N. (2012). *Molecular Fluorescence:
   Principles and Applications*, 2nd ed. Wiley-VCH.
   DOI: 10.1002/9783527650002.

3. Singer, V. L., Jones, L. J., Yue, S. T. & Haugland, R. P. (1997).
   Characterization of PicoGreen Reagent and Development of a
   Fluorescence-Based Solution Assay for Double-Stranded DNA Quantitation.
   *Analytical Biochemistry*, 249(2), 228–238.
   DOI: 10.1006/abio.1997.2177.

4. Promega Corporation (2022). *QuantiFluor® ONE dsDNA System Technical
   Manual*, TM405, Revised 10/22.
   https://www.promega.com/resources/protocols/technical-manuals/101/quantifluor-one-dsdna-system-protocol/

5. Promega Corporation (2024). *Quantus™ Fluorometer Operating Manual*,
   TM396, Revised 11/24.
   https://www.promega.com/resources/protocols/technical-manuals/101/quantus-fluorometer-operating-manual-protocol/

6. DIN (2017). *DIN 38402-51:2017-05: German Standard Methods for the
   Examination of Water, Waste Water and Sludge — General Information —
   Part 51: Calibration of Analytical Methods — Linear Calibration (A 51)*.
   DOI: 10.31030/2657448.

7. DIN (2008). *DIN 32645:2008-11: Chemical Analysis — Decision Limit,
   Detection Limit and Determination Limit under Repeatability Conditions —
   Terms, Methods, Evaluation*. DOI: 10.31030/1465413.

8. Anderson, W. et al. (2024). *DIYNAFLUOR: An Affordable DIY Plug-and-Play
   Nucleic Acid Fluorometer for eDNA Quantification in Resource Limited
   Settings*. bioRxiv. Preprint.
   DOI: 10.1101/2024.12.16.626200.

9. Trau Lab. *DIYNAFLUOR: Code, 3D Print Files, BOM and Build Instructions*.
   https://github.com/traulab/DIYNAFLUOR

10. ioRodeo. *Open Colorimeter Plus Firmware*.
    https://github.com/iorodeo/open_colorimeter_plus_firmware

11. ioRodeo. *Fixed-Current Radial 16 mA LED Board,
    ver_0p1_rev_3*.
    https://github.com/iorodeo/i_control_led/tree/main/fixed/5V_regulator/radial_16mA/production/ver_0p1_rev_3

12. IO Rodeo. *Fluorometer Tube Holder*.
    https://github.com/iorodeo/fluorometer_tube_holder

13. Long, J. (2024). *DNA Quantification with the UV Open Colorimeter*.
    IO Rodeo Blog, 26 August 2024.
    https://blog.iorodeo.com/uv-dna-quantification/

14. Long, J. (2023). *DNA Quantitation with the Open Colorimeter Plus*.
    IO Rodeo Blog, 8 August 2023.
    https://blog.iorodeo.com/open-colorimeter-plus-dna-quantitation/

15. Long, J. & Dickson, W. (2025). *Open Colorimeter Plus Firmware and
    Hardware Updates*. IO Rodeo Blog, 5 January 2025.
    https://blog.iorodeo.com/open-colorimeter-plus-firmware-and-hardware-updates/

16. Adafruit Industries. *Adafruit PyBadge, Product ID 4200*.
    https://www.adafruit.com/product/4200

17. Adafruit Industries. *TSL2591 High Dynamic Range Digital Light Sensor,
    Product ID 1980*.
    https://www.adafruit.com/product/1980

18. Adafruit Industries. *PCA9546 4-Channel I²C Multiplexer,
    Product ID 5664*.
    https://www.adafruit.com/product/5664

19. Adafruit Industries (2024). *CircuitPython for Adafruit PyBadge*,
    version 9.1.1.
    https://circuitpython.org/board/pybadge/

20. Wright, L. *PySpectrometer2*.
    https://github.com/leswright1977/PySpectrometer2

21. SparkFun Electronics. *Qwiic Adapter Cable, Product PRT-15109*.
    https://www.sparkfun.com/products/15109

22. Neemoo. *Optical Band-Pass Filters, AliExpress Item
    1005010613836251*.
    https://de.aliexpress.com/item/1005010613836251.html

---

⬅️ Previous Chapter: [Workshop Review, Quality Check and Further Applications](12_workshop_exercises_and_checklists.md)

📖 [Documentation Summary](SUMMARY.md)

➡️ Next Chapter: [Appendices](14_appendices.md)

