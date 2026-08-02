# DIY-QuantiFluorONE-dsDNA-Fluorometer

> **Repository status:** Draft  

> **Release:** v0.1.2-draft.1  

> **Validation status:** Not yet validated  

> **Documentation language:** English

The **DIY-QuantiFluorONE-dsDNA-Fluorometer**, abbreviated **DIY-QFO**, is an independently developed, portable, and modular fluorometer project for the fluorometric quantification of double-stranded DNA (**dsDNA**).
Its modular optical design allows excitation LED boards, kuvette holders and optical filters to be exchanged. This makes it possible to adapt the instrument to other dsDNA fluorescence assays and, after appropriate hardware configuration, calibration, and validation, to additional fluorescence-based analytical applications.

The instrument is designed for use with the **Promega QuantiFluor® ONE dsDNA System**. It integrates:

- the **Adafruit PyBadge** as the instrument control and user-interface platform;

- modified firmware derived from the open-source **ioRodeo Open Colorimeter Plus** project; and

- a modified 3D-printed sample holder derived from the open-source **DIYNAFLUOR** project.

The instrument is intended for use during the **[project name]** in Malaysia in cooperation with members of the **Leibniz Centre for Tropical Marine Research (ZMT)** and **[partner institution or organisation]**.

## Important status statement

Software stability, documentation maturity, hardware maturity, and analytical validation are controlled independently.

A software component marked **Stable** is not automatically analytically **Validated**. Likewise, a completed hardware or documentation release does not imply that the complete measurement procedure has passed final validation.

Preliminary, draft, stable, validated, and final materials are identified separately throughout this repository.

## Project objectives

The project aims to provide a compact and comprehensively documented fluorometer system for:

- teaching and laboratory workshops;

- preparation and measurement of dsDNA calibration standards;

- two-point and multipoint calibration;

- transfer and use of calibration JSON files;

- measurement of dsDNA samples using the Promega QuantiFluor® ONE dsDNA System;

- evaluation of calibration performance, residuals, LOD, LOQ, precision, and repeatability; and

- reproducible documentation of hardware, firmware, calibration, and validation procedures.

## Documentation

- [Documentation index](docs/markdown/index.md)

- Workshop booklet:  

  `docs/pdf/a4/DIY-QuantiFluorONE-dsDNA-Fluorometer_Workshop_Booklet_A4.pdf`

- Quick-start guides:  

  `docs/quick_start_guides/`

- Editable documentation source files:  

  `docs/source_files/` and `docs/workshop_booklet/`

- Figures and diagrams:  

  `docs/figures/`

- References:  

  `docs/references/`

The workshop booklet is intended to be sufficiently self-contained for the basic installation, calibration, and dsDNA measurement exercises. Participants should not need to browse the complete GitHub repository during the practical workshop sessions.

## Repository map

- `firmware/` — PyBadge firmware, configuration files, libraries, and user-interface assets

- `calibration_suite/` — Calibration Suite 7.2 Stable and supporting files

- `calibration_files/` — calibration JSON templates, examples, and released calibration files

- `hardware/` — mechanical, PCB, optical, and electronic design files

- `bom/` — bill of materials, supplier information, alternatives, and cost records

- `validation/` — protocols, raw data, processed data, analysis, and validation reports

- `docs/` — synchronized Markdown and PDF documentation

- `examples/` — example CSV, JSON, and workshop datasets

- `tests/` — software, data-format, and documentation tests

- `releases/` — release manifests and archived release information

## System architecture

The DIY-QFO combines the following principal components:

- an Adafruit PyBadge control and display unit;

- one excitation LED;

- an optical excitation path;

- a sample vessel or reaction tube;

- an emission filter;

- one TSL2591 light sensor;

- a 3D-printed optical and mechanical assembly; and

- firmware for measurement, calibration handling, result display, and data export.

Detailed component specifications and revision-controlled hardware information are provided in the `hardware/`, `bom/`, and `docs/` directories.

## Optical architecture

## Optical architecture

The instrument uses one TSL2591 light sensor positioned at 90° to the excitation beam.

Fluorescence emitted by the stained dsDNA sample passes through the emission filter and is detected by the TSL2591 sensor.

Calibration is based on the blank-corrected fluorescence signal:

\[
S_{\mathrm{corrected}} = S_{\mathrm{sample}} - S_{\mathrm{blank}}
\]

The corrected fluorescence signal is related to dsDNA concentration using either a two-point calibration (**2PT**) or a multipoint calibration (**MP**), depending on the selected procedure.

## Calibration

The repository distinguishes between:

- **2PT calibration** — two-point calibration using a blank or low standard and a defined higher-concentration standard;

- **MP calibration** — multipoint calibration using several concentration levels across the intended measurement range.

Calibration measurements may be processed using **Calibration Suite 7.2 Stable**. Calibration results can be exported as JSON files and transferred to the fluorometer.

The applicable calibration model, concentration range, units, regression method, LOD and LOQ procedure, residual evaluation, and validity criteria must be documented for every released calibration.

## Safety and intended use

The DIY-QuantiFluorONE-dsDNA-Fluorometer is intended as a research, teaching, development, and workshop instrument.

It is not a medical device and must not be used for:

- clinical diagnostic decisions;

- patient testing;

- therapeutic decisions;

- forensic conclusions; or

- any other regulated diagnostic application.

Users are responsible for following the safety instructions supplied with all reagents, DNA standards, batteries, electronic components, laboratory equipment, and consumables.

## Validation status

The complete analytical procedure has not yet passed final validation.

Current results, when available, must be identified as one of the following:

- example data;

- preliminary experimental data;

- preliminary validation data;

- quality-controlled validation data; or

- final validated data.

Preliminary results must not be presented as final performance specifications.

## Citation

Citation metadata are maintained in [`CITATION.cff`](CITATION.cff).

A formal citation will be added when the first citable project release is published.

## License

License selection is currently pending.

Hardware files, firmware, documentation, datasets, photographs, diagrams, and third-party components may require separate licenses or attribution notices. Until the applicable licenses have been confirmed, repository contents must not be assumed to be available for unrestricted reuse or redistribution.

Third-party source files must retain their original copyright, license, and attribution information.

## Trademark and affiliation notice

**Promega**, **QuantiFluor**, and **Quantus** are trademarks or registered trademarks of Promega Corporation or its affiliates.

The DIY-QuantiFluorONE-dsDNA-Fluorometer is an independent DIY project. It is not an official Promega product and is not presented as being endorsed, certified, validated, manufactured, or supported by Promega Corporation.

The references to the Promega QuantiFluor® ONE dsDNA System and the Promega Quantus™ Fluorometer are provided solely to identify the intended reagent system and a relevant commercial comparison instrument.

## Acknowledgements

The project builds upon concepts, source code, mechanical designs, or documentation from the following open-source projects:

- **ioRodeo Open Colorimeter Plus**

- **DIYNAFLUOR**

Complete references, original licenses, modification notes, and attribution information will be maintained in the documentation and third-party notices.

## Contact

**Project lead:** [Matthias Birkicht]  

**Institution:** [Leibniz Centre for Marine Tropical Research]  

**Project:** [Project name]  

**Contact:** [LZMT, Fahrenheitstraße 6, D-28359 Bremen, Germany]
