# DIY-QuantiFluorONE-dsDNA-Fluorometer

> **Repository status:** Draft  
> **Release:** v0.1.2-draft.1  
> **Validation status:** Not yet validated  
> **Documentation language:** English

The **DIY-QuantiFluorONE-dsDNA-Fluorometer** (short name: **DIY-QFO**) is an independently developed, open, portable fluorometer project for fluorometric quantification of double-stranded DNA. It is designed for use with the **Promega QuantiFluor® ONE dsDNA System** and is based on an Adafruit PyBadge instrument platform.

The project name identifies the DIY instrument and documentation system. It must not be shortened to “QuantiFluorONE”, because that wording could be confused with the Promega reagent system.

## Important status statement

Software stability, documentation maturity, and analytical validation are controlled independently. A component marked **Stable** is not automatically **Validated**.

## Documentation

- [Documentation index](docs/markdown/index.md)
- Workshop booklet: `docs/pdf/a4/DIY-QuantiFluorONE-dsDNA-Fluorometer_Workshop_Booklet_A4.pdf`
- Quick-start guides: `docs/quick_start_guides/`
- Source files: `docs/source_files/` and `docs/workshop_booklet/`

## Repository map

- `firmware/` — PyBadge firmware, configuration, libraries, and UI assets
- `calibration_suite/` — Calibration Suite 7.2 Stable and supporting files
- `hardware/` — mechanical, PCB, optical, and electronic design files
- `validation/` — protocols, raw data, processed data, analysis, and reports
- `docs/` — synchronized Markdown and PDF documentation
- `examples/` — example CSV, JSON, and workshop datasets

## Safety and intended use

The DIY-QuantiFluorONE-dsDNA-Fluorometer is a research, teaching, and workshop instrument. It is not a medical device and must not be used for clinical diagnostic decisions.

## Optical architecture

The instrument uses **one TSL2591 fluorescence sensor** positioned approximately 90° to the excitation beam. It does not include a 180° reference or transmission sensor. Calibration is based on the blank-corrected 90° fluorescence response.

## Citation

Citation metadata will be maintained in `CITATION.cff`.

## License

License selection is pending. Hardware, software, documentation, datasets, and third-party components may require separate license notices.

## Trademark and affiliation notice

Promega, QuantiFluor, and Quantus are trademarks or registered trademarks of Promega Corporation or its affiliates. This independent DIY project is not an official Promega product and is not presented as being endorsed, certified, or manufactured by Promega Corporation.
