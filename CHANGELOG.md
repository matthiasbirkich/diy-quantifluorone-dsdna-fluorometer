# Changelog

All notable changes to the DIY-QuantiFluorONE-dsDNA-Fluorometer will be documented here.

## [Unreleased]

No unreleased changes at this time.

## [1.0.0] - 2026-08-10

### Added
- Final workshop booklet for the 2026 eDNA workshop within the STABLE Project.
- Validated analytical-performance documentation for the documented hardware and assay configuration.
- Final hardware, software, calibration, validation, references, and workshop documentation structure.
- MIT License and completed citation metadata.
- Prominent workshop entry points through the GitHub Markdown documentation and downloadable PDF booklet.
- Source and provenance references for ioRodeo, DIYNAFLUOR, Adafruit, Promega, PySpectrometer2, standards, optical filters, and related hardware.

### Changed
- Consolidated the workshop documentation into the final 14-chapter structure.
- Updated project metadata and repository documentation for release `v1.0.0`.
- Updated analytical status terminology to distinguish operational calibration status from method-performance status.
- Updated the documented optical geometry to one TSL2591 sensor fixed at 90° to the excitation axis.
- Simplified the repository structure and removed obsolete development scaffolds and redundant directories.
- Updated the software layout to one supported QuantiFluorONE firmware package under `software/`.
- Updated the Calibration Suite and calibration-transfer documentation to the validated workflow.
- Updated references, acknowledgements, third-party attribution, and mechanical-source documentation.

### Verified
- Operational calibration status: `ACTIVE`.
- Method performance status: `VERIFIED`.
- Operational range: 0–400 ng/µL dsDNA.
- Documented firmware environment: CircuitPython 9.1.1 and QuantiFluorONE QF1-1.0.0-rc2.
- Calibration Suite: v7.2 Stable.

## [0.1.2-draft.1] - 2026-08-02

### Changed
- Renamed the project from `QuantiFluorONE` to `DIY-QuantiFluorONE-dsDNA-Fluorometer`.
- Introduced the controlled short name `DIY-QFO` and repository slug `diy-quantifluorone-dsdna-fluorometer`.
- Clarified the distinction between the DIY instrument and the Promega QuantiFluor® ONE dsDNA System.
- Updated document titles, metadata, identifiers, booklet sources, and citation metadata.

## [0.1.1-draft.1] - 2026-08-02

### Changed
- Corrected the optical architecture to a single TSL2591 sensor at approximately 90° to the excitation beam.
- Removed all 180° reference-channel and fluorescence/reference-ratio terminology.
- Defined the calibration response as the blank-corrected 90° fluorescence signal.

## [0.1.0-draft.1] - 2026-08-02

### Added
- Initial repository and documentation structure.