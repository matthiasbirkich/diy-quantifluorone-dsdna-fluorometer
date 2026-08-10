## eDNA Workshop 2026 — Start Here

**Workshop participants:** 
You do not need to navigate the repository structure to get started.

### Start the Workshop

➡️ **[Start the Workshop](docs/markdown/SUMMARY.md)**

The online documentation guides you step by step through the workshop,
from the introduction and instrument assembly to software installation,
calibration, dsDNA measurement, quality control, and troubleshooting.
For sequential reading, use the chapter navigation provided in the
documentation.

### 📘 Complete Workshop Booklet

The complete workshop documentation is also available as a PDF for

offline use, printing, or download:

➡️ **[Download the complete Workshop Booklet (PDF)](00_DIY-QuantiFluorONE_Workshop_Handbook.pdf)**

The PDF is approximately 30 MB and may not be previewed directly by GitHub.

Downloading the file is therefore recommended.

### Repository contents

The folders in this repository contain the hardware files, software,
Calibration Suite, validation data, references, and editable documentation
used to reproduce the project.

The workshop booklet is the primary guide for assembly, software installation,
basic operation, calibration, quality control, dsDNA measurement, validation,
and troubleshooting.

It guides participants through:

1. instrument overview and measurement principle;
2. safety and laboratory preparation;
3. hardware and assembly;
4. software installation;
5. basic operation and menu navigation;
6. calibration and data transfer;
7. dsDNA measurement;
8. calibration, results, and quality control;
9. validation and analytical performance; and
10. troubleshooting and workshop review.

The folders in this repository contain the source files, hardware documentation,
software, calibration tools, validation data, references, and editable workshop
documentation used to reproduce the project.

## About the project

The **DIY-QuantiFluorONE-dsDNA-Fluorometer**, abbreviated **DIY-QFO**, is an
independently developed portable fluorometer for fluorometric quantification
of double-stranded DNA (**dsDNA**).

The instrument is designed for use with the **Promega QuantiFluor® ONE dsDNA
System** and combines:

- an **Adafruit PyBadge** as controller, display, and user interface;
- one **TSL2591** fluorescence sensor positioned at 90° to the excitation axis;
- an **ioRodeo fixed-current radial 16 mA LED board**;
- a 485 nm excitation LED;
- Neemoo Ex470BP-40 and Em532BP-40 optical band-pass filters;
- a modified 3D-printed optical sample holder derived from concepts used by
  **DIYNAFLUOR** and the **ioRodeo fluorometer tube-holder project**; and
- modified firmware derived from the open-source **ioRodeo Open Colorimeter
  Plus** project.

The modular optical design allows LEDs, filters, sample holders, and detector
settings to be adapted for other fluorescence-based analytical applications,
provided that the modified configuration is appropriately calibrated and
evaluated.

## Workshop context

This repository and the accompanying workshop booklet were prepared for the
**eDNA Workshop 2026** within the **STABLE Project (2025–2027), Higher
Education Partnership for a Sustainable Blue Economy**.

The workshop uses the DIY-QFO as an open and reproducible platform for
introducing fluorometric dsDNA quantification, instrument construction,
calibration, quality control, and analytical evaluation.

The instrument is intended for **research, teaching, development, and workshop
measurements**. It is not intended for clinical diagnostic use.

## Documentation

The complete workshop documentation is available in several forms:

- **Workshop Booklet (PDF)** — primary document for workshop participants;
- `workshop_booklet/` — Quarto source used to generate the booklet;
- `docs/` — project documentation and figures;
- `references/` — bibliography and project source/provenance records.

For workshop participation, the PDF booklet is the recommended starting point.
Participants do not need to navigate the complete repository during the
practical exercises.

## Repository map

The principal project directories are:

- **`bom/`** — bill of materials and component information;
- **`docs/`** — project documentation and figures;
- **`hardware/`** — mechanical CAD models, PCB files, wiring information, and
  hardware documentation;
- **`references/`** — bibliography and source/provenance records;
- **`software/`** — PyBadge bootloader, CircuitPython, and the supported
  QuantiFluorONE firmware release;
- **`tools/`** — Calibration Suite and supporting analytical utilities;
- **`validation/`** — analytical validation datasets, processed data, and
  evaluation scripts;
- **`workshop_booklet/`** — Quarto sources for the workshop booklet.

This structure separates hardware, software, analytical tools, validation
evidence, references, and documentation while maintaining traceability between
the documented instrument and the files required to reproduce it.

## Optical architecture

The DIY-QFO uses one TSL2591 fluorescence sensor positioned **at 90°** to the
excitation axis.

The documented configuration uses:

- 485 nm excitation LED;
- Neemoo Ex470BP-40, 8 × 8 × 1 mm excitation filter;
- Neemoo Em532BP-40, 8 × 8 × 1 mm emission filter; and
- Promega E4941 thin-walled 0.5 mL PCR tubes.

Fluorescence emitted by the stained dsDNA sample passes through the emission
filter and is detected by the TSL2591.

The project-defined visible analytical signal is:

\[
VIS = FULL - IR
\]

and the blank-corrected fluorescence response is used for calibration and
concentration calculation.

## Calibration and analytical performance

The firmware supports an on-instrument two-point calibration and import of a
compatible multipoint calibration.

Routine operation uses a two-point calibration consisting of a reagent blank
and a nominal 400 ng/µL lambda-DNA standard.

Under the tested configuration and assay conditions, method performance was
evaluated over an operational range of:

**0–400 ng/µL dsDNA**

The validation study showed close agreement with a Promega Quantus Fluorometer
used as an independent external comparator.

The project currently uses approximately:

- **LOD: 8 ng/µL**
- **LOQ: 24 ng/µL**

on the original-sample concentration basis.

Detailed calibration procedures, quality-control requirements, statistical
evaluation, validation results, and limitations are documented in the workshop
booklet and under `validation/`.

## Software

The documented software configuration is:

- **PyBadge UF2 bootloader:** 3.15.0
- **Adafruit CircuitPython:** 9.1.1
- **QuantiFluorONE firmware:** QF1-1.0.0-rc2

The supported firmware package is stored under:

`software/quantifluorone_firmware/`

The repository follows a **one instrument — one supported firmware release**
policy for the documented workshop configuration.

## Safety and intended use

The DIY-QuantiFluorONE-dsDNA-Fluorometer is intended as a research, teaching,
development, and workshop instrument.

It is not a medical device and must not be used for:

- clinical diagnostic decisions;
- patient testing;
- therapeutic decisions;
- forensic conclusions; or
- other regulated diagnostic applications.

Users are responsible for following the safety instructions supplied with all
reagents, DNA standards, batteries, electronic components, laboratory equipment,
and consumables.

## Reproducibility and source records

Project-specific source and provenance records are maintained in:

- `references/references.bib`
- `references/hardware_sources.yml`
- `references/source_register.csv`
- `references/standards_register.md`

Component-specific source files, licences, and attribution information are
retained with the corresponding hardware and software documentation where
applicable.

## Citation

Citation metadata are maintained in [`CITATION.cff`](CITATION.cff).

Please use the citation information associated with the corresponding project
release when referencing the DIY-QuantiFluorONE-dsDNA-Fluorometer.

## License and third-party material

The repository contains original project material as well as components,
concepts, software, and design files derived from or based on third-party
open-source projects.

Third-party materials retain their respective copyright, licence, and
attribution requirements. Consult the component-specific licence files,
source records, and repository documentation before reuse or redistribution.

## Trademark and affiliation notice

**Promega**, **QuantiFluor**, and **Quantus** are trademarks or registered
trademarks of Promega Corporation or its affiliates.

The DIY-QuantiFluorONE-dsDNA-Fluorometer is an independent DIY project. It is
not an official Promega product and is not presented as being endorsed,
certified, manufactured, or supported by Promega Corporation.

References to the Promega QuantiFluor® ONE dsDNA System and Promega Quantus™
Fluorometer identify the reagent system and commercial comparison instrument
used in the documented project.

## Acknowledgements

The project builds upon concepts, source code, mechanical designs, and
documentation from open-source projects including:

- **ioRodeo Open Colorimeter Plus**
- **ioRodeo fluorometer tube holder**
- **DIYNAFLUOR**
- **Adafruit CircuitPython**
- **PySpectrometer2**

The modified mechanical parts and their integration into the
DIY-QuantiFluorONE-dsDNA-Fluorometer were developed collaboratively by
**Dipl.-Ing. Matthias Birkicht** and **Florian Bock, 3D-Haven, Bremerhaven,
Germany**.

Complete references, licences, modification notes, and attribution information
are maintained in the project documentation and source records.

## Contact and project context

**Project author:** Dipl.-Ing. Matthias Birkicht

**eDNA Workshop 2026:** with Dr. Achim Meyer

**Workshop context:** STABLE Project (2025–2027), *Higher Education Partnership
for a Sustainable Blue Economy*

For technical details, reproducibility information, and source attribution,
consult the workshop booklet and the documentation contained in this repository.