# DIY-QuantiFluorONE-dsDNA-Fluorometer Documentation Blueprint

**Document status:** Draft  
**Blueprint version:** 0.1.2-draft.1  
**Date:** 2026-08-02  
**Repository language:** English  
**Communication language:** German

## 1. Proposed repository structure

The repository should separate editable source files, generated documentation, software, hardware, calibration files, and evidence from validation experiments. Generated Markdown and PDF files must not be edited manually.

```text
diy-quantifluorone-dsdna-fluorometer/
├── README.md
├── LICENSE
├── CITATION.cff
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── .gitignore
├── .gitattributes
├── .github/
│   ├── workflows/
│   │   ├── build-documentation.yml
│   │   ├── validate-calibration-json.yml
│   │   └── create-release-package.yml
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
├── metadata/
│   ├── project_metadata.yml
│   ├── terminology.yml
│   ├── document_control.yml
│   └── release_manifest.yml
├── docs/
│   ├── markdown/                         # generated GitHub Markdown
│   ├── pdf/
│   │   ├── a4/                          # primary print format
│   │   ├── a5/                          # optional booklet format
│   │   └── individual_guides/
│   ├── workshop_booklet/                # Quarto book project
│   │   ├── _quarto.yml
│   │   ├── index.qmd
│   │   ├── chapters/
│   │   ├── appendices/
│   │   ├── styles/
│   │   └── includes/
│   ├── quick_start_guides/
│   ├── figures/
│   │   ├── source/
│   │   ├── svg/
│   │   ├── png/
│   │   └── photos/
│   ├── tables/
│   ├── references/
│   │   ├── references.bib
│   │   ├── standards_register.md
│   │   └── source_register.csv
│   └── source_files/                    # canonical reusable content
│       ├── content/
│       ├── templates/
│       └── scripts/
├── firmware/
│   └── pybadge/
│       ├── src/
│       ├── lib/
│       ├── config/
│       ├── assets/
│       ├── releases/
│       └── tests/
├── calibration_suite/
│   ├── source/
│   ├── v7.2-stable/
│   ├── examples/
│   ├── schemas/
│   └── tests/
├── calibration_files/
│   ├── templates/
│   ├── examples/
│   └── validated/
├── hardware/
│   ├── mechanical/
│   │   ├── cad_source/
│   │   ├── stl/
│   │   ├── step/
│   │   └── print_profiles/
│   ├── pcb/
│   │   ├── kicad/
│   │   ├── gerber/
│   │   ├── drill/
│   │   ├── assembly/
│   │   │   ├── bom/
│   │   │   └── cpl/
│   │   └── fabrication_notes/
│   ├── optics/
│   └── electronics/
├── bom/
│   ├── master_bom.csv
│   ├── suppliers.csv
│   ├── cost_history.csv
│   └── alternates.csv
├── validation/
│   ├── protocols/
│   ├── preliminary/
│   │   ├── raw/
│   │   ├── processed/
│   │   ├── notebooks/
│   │   └── reports/
│   ├── final/
│   │   ├── raw/
│   │   ├── processed/
│   │   ├── notebooks/
│   │   └── reports/
│   ├── qc/
│   └── acceptance_criteria/
├── examples/
│   ├── csv/
│   ├── json/
│   └── workshop/
├── tests/
│   ├── hardware/
│   ├── firmware/
│   ├── calibration_suite/
│   └── documentation/
├── tools/
│   ├── build_docs/
│   ├── validate_metadata/
│   ├── validate_json/
│   └── release/
└── releases/
    └── manifests/
```

### Repository rules

1. Canonical text is stored in `docs/source_files/` and `docs/workshop_booklet/`.
2. `docs/markdown/` and `docs/pdf/` contain generated output.
3. Raw validation data are immutable after import.
4. Processed data must identify the raw source file and analysis version.
5. Calibration JSON files require a schema version, device identifier, assay, calibration mode, date, software version, and validation status.
6. Each released document must display project version, document revision, status, date, and validation statement.

## 2. Controlled terminology and abbreviation list

| Preferred term | Abbreviation | Controlled definition and use | Avoid or qualify |
|---|---:|---|---|
| DIY-QuantiFluorONE-dsDNA-Fluorometer | DIY-QFO | The independently developed instrument, firmware, calibration workflow, and documentation system. | Do not use “QuantiFluorONE” alone as the project name. |
| QuantiFluor® ONE dsDNA System | QF ONE | The Promega reagent system. Preserve the official product name in formal text. | Clearly distinguish it from the DIY instrument. |
| Quantus™ Fluorometer | — | Promega commercial reference fluorometer. | Do not shorten to “Quantus system” in comparison tables. |
| ioRodeo Open Colorimeter Plus | OCP | Open hardware platform used as a design and documentation reference. | Distinguish from the earlier Open Colorimeter. |
| DIYNAFLUOR | — | Open-source nucleic-acid fluorometer used as a comparison system. | Preserve capitalization. |
| Adafruit PyBadge | PyBadge | Microcontroller/display platform used by DIY-QuantiFluorONE-dsDNA-Fluorometer. | State exact board revision when known. |
| double-stranded DNA | dsDNA | Target analyte. Define at first use. | Avoid “DNA” when ssDNA/RNA selectivity matters. |
| lambda DNA | λ-DNA | dsDNA reference material derived from bacteriophage lambda. | State supplier, product, lot, stock concentration, and matrix. |
| excitation wavelength | λ_ex | Wavelength or band used to excite the fluorophore. | Do not describe LED peak wavelength as a monochromatic wavelength. |
| emission wavelength | λ_em | Wavelength or band of emitted fluorescence. | Distinguish dye maximum from filter passband. |
| fluorescence channel | 90° channel | The single TSL2591 detector channel positioned approximately perpendicular to the excitation beam to measure emitted fluorescence. | DIY-QuantiFluorONE-dsDNA-Fluorometer has no 180° reference or transmission sensor. |
| raw sensor signal | — | Uncorrected TSL2591 output or project-defined sensor count. | Do not call it RFU unless normalized/defined. |
| blank-corrected signal | — | Sample signal minus corresponding blank signal. | Never use negative values without stating handling rules. |
| blank-corrected fluorescence response | ΔS | Difference between the 90° sample signal and the corresponding 90° blank signal: ΔS = S_sample − S_blank. | Do not describe the response as a fluorescence/reference ratio. |
| relative fluorescence unit | RFU | Relative, instrument-dependent signal unit. | Never imply SI traceability. |
| reagent blank | blank | Reagent mixture prepared without dsDNA sample or standard. | Distinguish from zero standard if matrices differ. |
| calibration standard | standard | Material with assigned dsDNA concentration used for calibration. | Do not use “sample” for standards in procedural steps. |
| two-point calibration | 2PT | Calibration based on two defined concentration levels. | Define point selection and regression/transform rules. |
| multipoint calibration | MP | Calibration using more than two concentration levels. | State weighting, model, and replicate handling. |
| calibration function | — | Mathematical relation between signal and concentration. | Distinguish from instrument configuration. |
| limit of detection | LOD | Detection limit calculated by the documented method. | Never report without method, confidence assumptions, units, and dataset. |
| limit of quantification | LOQ | Quantification limit calculated by the documented method. | Never equate automatically with the lowest standard. |
| working range | — | Concentration interval meeting defined validity criteria. | Distinguish from nominal reagent range. |
| repeatability | — | Precision under repeatability conditions. | Do not use interchangeably with reproducibility. |
| recovery | % recovery | Measured concentration relative to assigned or spiked concentration. | State matrix and calculation. |
| short press | — | Button actuation below the defined duration threshold. | Threshold must be specified in firmware documentation. |
| long press | — | Button actuation at or above the defined duration threshold. | Threshold must be specified and tested. |
| Calibration Suite 7.2 Stable | CS 7.2 | Exact software release used for calibration processing. | “Stable” describes release maturity, not analytical validation. |

### Style rules

- Use a space between value and unit: `200 µL`, `531 nm`, `25 °C`.
- Use `ng/µL` consistently for sample concentration unless another unit is required.
- Use decimal points in English documentation.
- Use ISO dates: `2026-08-02`.
- Use “Figure 3” and “Table 2” in prose; automatic numbering is preferred.
- Define abbreviations at first use in every stand-alone guide.
- Use “shall” only for mandatory controlled requirements; use “should” for recommendations and “may” for options.

## 3. Documentation status and versioning system

### 3.1 Independent status axes

A single status label is insufficient. Each controlled file should carry three independent fields.

| Axis | Allowed values | Meaning |
|---|---|---|
| Document status | Draft → Review → Approved → Final | Editorial and approval maturity. |
| Software status | Experimental → Preliminary → Stable → Deprecated | Software maturity and compatibility. |
| Validation status | Not validated → Preliminary validation → Partially validated → Validated | Strength of analytical evidence. |
| Data status | Synthetic → Example → Preliminary → Quality-controlled → Final → Archived | Evidentiary role of a dataset. |

**Mandatory rule:** “Stable” must never be interpreted as “Validated.”

### 3.2 Version format

Use Semantic Versioning for repository releases:

```text
MAJOR.MINOR.PATCH[-PRERELEASE]
```

Examples:

- `0.1.2-draft.1` — initial documentation structure;
- `0.5.0-preliminary.1` — workshop-capable but not fully validated;
- `0.9.0-rc.1` — release candidate;
- `1.0.0` — first approved stable repository release;
- `1.1.0` — backward-compatible new functionality;
- `1.1.1` — corrections without intended workflow changes;
- `2.0.0` — incompatible hardware, file-format, or workflow change.

### 3.3 Controlled document header

Every stand-alone guide and booklet shall show:

```yaml
project: DIY-QuantiFluorONE-dsDNA-Fluorometer
document_title: "..."
document_id: DIY-QFO-DOC-...
project_version: 0.1.2-draft.1
document_revision: 0.1
document_status: Draft
software_status: Preliminary
validation_status: Not validated
release_date: 2026-08-02
author: "[Name]"
approver: "[Name or pending]"
```

### 3.4 Identifier conventions

| Item | Pattern | Example |
|---|---|---|
| Document | `DIY-QFO-DOC-NNN` | `DIY-QFO-DOC-001` |
| Figure | automatic chapter numbering | `Figure 7.3` |
| Table | automatic chapter numbering | `Table 5.2` |
| Hardware revision | `DIY-QFO-HW-Rx.y` | `DIY-QFO-HW-R1.0` |
| Firmware release | `DIY-QFO-FW-vX.Y.Z` | `DIY-QFO-FW-v1.0.0` |
| Calibration Suite | `DIY-QFO-CS-vX.Y.Z` | `DIY-QFO-CS-v7.2.0` |
| Calibration file | `DIY-QFO_CAL_<device>_<assay>_<mode>_<date>_vX.Y.Z.json` | `DIY-QFO_CAL_001_DIY-QFONE_MP_2026-08-02_v1.0.0.json` |
| Raw dataset | `DIY-QFO_RAW_<study>_<date>_<run>` | `DIY-QFO_RAW_PREVAL_2026-08-02_RUN01.csv` |
| Processed dataset | `DIY-QFO_PROC_<study>_<date>_<analysis-version>` | `DIY-QFO_PROC_PREVAL_2026-08-02_v0.3.0.csv` |

### 3.5 Release gates

A `Final` or `Validated` release requires:

1. complete release manifest;
2. successful documentation build;
3. valid JSON schemas and examples;
4. traceable BOM and hardware revision;
5. archived raw validation data;
6. reproducible processing scripts/notebooks;
7. acceptance criteria and signed review record;
8. safety review;
9. license and third-party attribution review;
10. checksum list for release artifacts.

## 4. Main README outline

1. **Project title, one-sentence purpose, and project image**
2. **Status banner**
   - repository version;
   - hardware revision;
   - firmware status;
   - validation status;
   - documentation status.
3. **Important validation and intended-use statement**
4. **What DIY-QuantiFluorONE-dsDNA-Fluorometer is**
5. **Key features**
6. **System overview diagram**
7. **Quick start**
   - obtain/build hardware;
   - install firmware;
   - load calibration;
   - perform blank and sample measurement.
8. **Documentation map**
   - online Markdown;
   - workshop booklet;
   - quick-start guides;
   - assembly guide;
   - calibration guide;
   - validation reports.
9. **Hardware overview**
10. **Software overview**
11. **Calibration modes: 2PT and MP**
12. **Calibration Suite 7.2 Stable**
13. **Example data and calibration files**
14. **Repository structure**
15. **Build the documentation locally**
16. **Validation status and known limitations**
17. **Safety**
18. **Troubleshooting and issue reporting**
19. **Contributing and change control**
20. **Citation**
21. **License and third-party notices**
22. **Acknowledgements and reference projects**

## 5. Detailed workshop booklet outline

### Front matter

- Title page
- Subtitle and workshop location
- Project version, document revision, status, and date
- Author, institution, contributors, and acknowledgements
- Intended-use and validation-status statement
- Copyright, license, trademarks, and third-party notices
- Revision history
- How to use this booklet
- Symbols for Safety, Warning, Important, Note, Quality Control, and Troubleshooting
- Table of contents
- List of figures
- List of tables

### Part I — Orientation and safety

#### 1. Introduction and learning objectives
- Project purpose
- Target users
- Workshop scope
- Learning outcomes
- Activities participants will complete
- Limits of the workshop result

#### 2. Safety and laboratory requirements
- General laboratory conduct
- Personal protective equipment
- Pipetting safety
- Reagent handling
- Electrical and battery safety
- 3D-printed-part and sharp-edge precautions
- Cleaning and contamination control
- Waste segregation and disposal
- Spill response
- Workshop-specific emergency information

#### 3. System overview
- Complete system photograph
- Functional block diagram
- Optical path
- Electronic architecture
- Data flow from sensor to concentration result
- Roles of firmware, configuration, calibration JSON, and Calibration Suite
- Contents of the workshop kit

#### 4. Fluorometric measurement principle
- Excitation and emission
- Fluorescence of DNA-binding dyes
- Spectral overlap of LED, filters, and dye
- Single-sensor 90° fluorescence geometry
- Blank correction
- Blank-corrected fluorescence response
- Relationship between signal and dsDNA concentration
- Sources of noise, drift, quenching, and non-linearity

### Part II — Hardware and software

#### 5. Hardware components
- PyBadge
- excitation LED and LED board
- optical filters
- TSL2591 sensors
- PCB and connectors
- Qwiic cables
- sample holder and reaction tubes
- enclosure and 3D-printed parts
- LiPo battery or power bank
- component specification table
- BOM and cost summary

#### 6. Assembly overview
- Required tools
- Printed-part inspection
- PCB preparation
- LED installation
- excitation-filter installation
- sensor installation
- emission-filter installation
- sample-holder installation
- cable routing
- battery installation
- optical alignment checks
- electrical inspection
- functional test
- assembly checklist

#### 7. PyBadge software installation
- Required computer and USB cable
- bootloader check and recovery
- CircuitPython installation
- required library bundle and versions
- firmware file structure
- copying source files
- copying configuration files
- copying UI assets
- safe eject and restart
- installed-version check
- recovery after failed installation
- common installation faults

#### 8. DIY-QuantiFluorONE-dsDNA-Fluorometer user interface
- Start screen
- measurement screen
- calibration screen
- status and error messages
- displayed concentration, uncertainty, LOD, and LOQ
- calibration-file information
- battery and sensor indicators
- data export behaviour

#### 9. Button-layout diagram
- labelled front-view diagram
- button names
- short-press functions
- long-press functions
- reserved functions
- screen-specific behaviour
- button-response troubleshooting

### Part III — Assay and calibration

#### 10. Preparation of standards and reagents
- Required consumables
- Promega reagent handling
- λ-DNA stock documentation
- dilution planning
- preparation of blank
- preparation of 2PT standards
- preparation of MP standards
- pipetting table
- mixing and incubation
- labelling strategy
- contamination control
- stability and storage notes

#### 11. Two-point calibration (2PT)
- intended use
- required standards
- replicate strategy
- blank measurement
- low/high standard measurement
- data-quality checks
- calibration calculation
- acceptance criteria
- saving and naming the result
- limitations of 2PT calibration

#### 12. Multipoint calibration (MP)
- intended use
- concentration range
- number and distribution of standards
- replicates
- measurement order
- drift controls
- model selection
- weighting
- residual evaluation
- outlier/rejection policy
- acceptance criteria
- calibration validity interval

#### 13. Calibration Suite 7.2 Stable
- installation and supported environments
- interface overview
- project setup
- CSV import requirements
- column definitions and units
- 2PT workflow
- MP workflow
- model and weighting options
- DIN-related calculations
- residual plots
- uncertainty outputs
- LOD and LOQ outputs
- audit information
- export functions
- known limitations

#### 14. Transfer of JSON calibration files
- JSON schema
- mandatory metadata
- export from Calibration Suite
- file naming
- transfer to PyBadge
- import in DIY-QuantiFluorONE-dsDNA-Fluorometer
- confirmation of active calibration
- rollback to previous calibration
- integrity and compatibility checks

### Part IV — Measurement and quality control

#### 15. Measurement of dsDNA samples
- sample requirements
- assay preparation
- incubation
- tube inspection
- vessel orientation
- blank measurement
- sample measurement
- replicate measurement
- result recording
- cleaning
- waste disposal

#### 16. Calculation and interpretation of results
- raw signals
- blank correction
- blank-corrected fluorescence response
- calibration equation
- dilution factor
- concentration in original sample
- rounding and significant figures
- uncertainty display
- below-LOD and below-LOQ reporting
- above-range reporting
- example calculation

#### 17. LOD and LOQ
- terminology
- project methods
- 2PT approach
- MP approach
- DIN 38402-51 and DIN 32645 applicability
- assumptions
- confidence parameters
- reporting requirements
- example output
- limitations

#### 18. Quality-control procedures
- daily/sequence blank
- check standard
- replicate criteria
- drift checks
- contamination checks
- control chart concept
- calibration validity
- recalibration triggers
- documentation requirements

#### 19. Troubleshooting
- device does not start
- CIRCUITPY drive does not appear
- missing library or import error
- sensor not detected
- LED not active
- signal saturation
- low signal
- unstable result
- blank too high
- negative corrected signal
- JSON not accepted
- calibration mismatch
- implausible concentration
- battery or USB problems
- escalation and issue-report template

### Part V — Evidence and comparison

#### 20. Preliminary and final validation results
- validation stages
- protocol identifiers
- hardware and software versions
- standards and range
- replicates
- raw-data availability
- processing workflow
- precision and repeatability
- recovery/accuracy
- LOD and LOQ
- working range
- deviations
- limitations
- acceptance criteria
- conclusions
- explicit separation of preliminary and final findings

#### 21. Performance comparison
- comparison principles and data-source hierarchy
- DIY-QuantiFluorONE-dsDNA-Fluorometer
- DIYNAFLUOR
- ioRodeo Open Colorimeter Plus
- Promega Quantus
- optional additional systems
- acquisition cost and cost date
- reagents and sample volume
- calibration flexibility
- sensitivity and range
- LOD/LOQ comparability limitations
- portability
- power supply
- repairability
- open-source availability
- teaching suitability
- field-laboratory suitability
- research suitability

### Part VI — Workshop activities

#### 22. Workshop exercises
- Exercise 1: identify hardware components
- Exercise 2: inspect or assemble the optical module
- Exercise 3: install or verify PyBadge software
- Exercise 4: prepare blank and standards
- Exercise 5: perform 2PT calibration
- Exercise 6: perform MP calibration
- Exercise 7: use Calibration Suite 7.2 Stable
- Exercise 8: transfer a calibration JSON file
- Exercise 9: measure unknown samples
- Exercise 10: evaluate QC and troubleshoot a faulty run
- answer sheets and expected outputs

#### 23. Checklists
- workshop preparation
- kit contents
- assembly inspection
- software installation
- calibration readiness
- measurement sequence
- QC review
- shutdown, cleaning, and storage

#### 24. References
- standards
- reagent manuals
- instrument manuals
- ioRodeo documentation
- DIYNAFLUOR repository and publication
- scientific fluorescence references
- statistical and validation references

#### 25. Appendices
- A. Complete BOM
- B. Wiring and connector table
- C. PCB revision and fabrication notes
- D. 3D-print settings
- E. Firmware file map
- F. Configuration-file reference
- G. Calibration JSON schema
- H. CSV schema
- I. Calculation formulas
- J. Dilution worksheets
- K. Acceptance criteria
- L. Troubleshooting decision tree
- M. Glossary and abbreviations
- N. Document history

## 6. Proposal for synchronized Markdown and PDF generation

### Recommended toolchain

- **Canonical authoring:** Quarto Markdown (`.qmd`) plus reusable YAML/CSV/BibTeX sources.
- **Rendering engine:** Quarto/Pandoc.
- **Primary PDF:** LaTeX/KOMA-Script A4 book.
- **Optional A5:** separate format profile; booklet imposition should be treated as a printing step, not merely page-size reduction.
- **GitHub output:** generated CommonMark/GitHub-compatible Markdown.
- **References:** one `references.bib` file.
- **Tables:** generated from controlled CSV files such as the BOM and comparison dataset.
- **Figures:** SVG as preferred master format; PNG for photographs and compatibility; PDF/SVG for print graphics.
- **Automation:** GitHub Actions builds and validates outputs on pull requests and release tags.

### Single-source workflow

```text
project_metadata.yml ─┐
terminology.yml       ├──> Quarto source modules ──> GitHub Markdown
references.bib        ┤                         ├──> A4 booklet PDF
BOM/comparison CSV    ┤                         ├──> A5 booklet PDF
figures and photos    ┘                         └──> individual PDF guides
```

### Content-management rules

1. Do not copy technical paragraphs manually between guides.
2. Reuse modules for safety, button functions, equations, terminology, and calibration steps.
3. Store version numbers and author data in metadata files.
4. Generate cost tables from CSV with a price date and currency.
5. Generate figure/table numbering automatically.
6. Use stable figure IDs and citation keys.
7. Add alt text to every informative figure.
8. Include status callouts automatically according to metadata.
9. Keep drafts in source control but exclude them from final release packages unless explicitly listed.
10. Build release PDFs only from a tagged commit.

### Output profiles

- `github`: GitHub-compatible Markdown, relative links, GitHub admonitions.
- `a4`: A4 portrait, print-friendly margins, headers/footers, page numbers.
- `a5`: A5 page layout with resized tables and figures.
- `guide`: individual A4 guide with its own title page and revision table.
- `review`: visible draft watermark and line numbers where useful.
- `release`: no watermark; only approved/final modules included.

### Automated checks

- broken links and missing figures;
- unresolved citations;
- duplicate figure/table IDs;
- metadata completeness;
- inconsistent terminology;
- stale generated outputs;
- JSON schema validation;
- CSV required columns and units;
- forbidden claims such as “validated” without approved validation evidence;
- release-manifest completeness.

## 7. Required-material checklist

The following items should be collected or confirmed before the repository can reach a stable workshop release.

### A. Project and document control

- [ ] Full author name(s), affiliations, ORCID identifiers, and contact information
- [ ] Project owner and document approver
- [ ] Workshop title, venue, city, Malaysia location, and date
- [ ] Funding and acknowledgement text
- [ ] Repository URL and access policy
- [ ] Intended-use statement
- [ ] License strategy for software, hardware, documentation, and data
- [ ] Trademark and third-party attribution wording

### B. Final hardware definition

- [ ] Final hardware revision number
- [ ] Complete system photograph
- [ ] Front, rear, side, and internal photographs
- [ ] Exploded-view or assembly diagram
- [ ] Exact PyBadge model/revision
- [ ] Exact PCB revision and KiCad source
- [ ] Gerber and drill files
- [ ] BOM and CPL used for PCB assembly
- [ ] PCB fabrication and assembly notes
- [ ] Exact LED manufacturer, part number, peak wavelength, viewing angle, current, and board configuration
- [ ] Exact excitation and emission filter part numbers, dimensions, orientation, and measured/nominal spectra
- [ ] Exact TSL2591 board type and address arrangement
- [ ] Qwiic cable lengths and routing
- [ ] LiPo battery/power-bank specification and safety information
- [ ] Connector and wiring table
- [ ] STL, STEP, and editable CAD source files
- [ ] 3D-print material, layer height, supports, orientation, tolerances, and post-processing
- [ ] Final sample-vessel specification and orientation mark
- [ ] Final total mass and external dimensions

### C. BOM, suppliers, and cost evidence

- [ ] Master BOM with quantities and alternates
- [ ] Supplier names and countries
- [ ] Supplier part numbers
- [ ] Unit prices, currency, quantity breaks, tax basis, shipping basis, and price date
- [ ] Workshop-kit cost
- [ ] Single-instrument cost
- [ ] PCB fabrication and assembly cost
- [ ] Consumables cost per assay
- [ ] Replacement-part recommendations
- [ ] Evidence or archived quotations for major cost claims

### D. Firmware and PyBadge installation

- [ ] Final firmware release files
- [ ] Exact bootloader version
- [ ] Exact CircuitPython version
- [ ] Required library bundle and individual library versions
- [ ] Complete `lib/` contents or reproducible dependency manifest
- [ ] Final `configuration.json`
- [ ] Final UI assets and source images
- [ ] Firmware checksum list
- [ ] Screenshots of every user-interface screen
- [ ] Final button map with short/long-press thresholds
- [ ] Error-message register and meaning
- [ ] CSV export schema
- [ ] Calibration JSON import behaviour
- [ ] Recovery procedure tested on a clean PyBadge
- [ ] Installation tests on Windows, macOS, and the intended workshop computers where applicable

### E. Calibration Suite 7.2 Stable

- [ ] Complete release package
- [ ] Source code and dependency manifest
- [ ] Supported operating systems
- [ ] Installation instructions
- [ ] Screenshots of the complete workflow
- [ ] Input CSV schema and examples
- [ ] Output JSON schema and examples
- [ ] 2PT algorithm specification
- [ ] MP algorithm specification
- [ ] Regression weighting options
- [ ] Residual and outlier rules
- [ ] Uncertainty calculation specification
- [ ] LOD/LOQ calculation specification
- [ ] DIN clause mapping based on licensed copies
- [ ] Unit tests and reference-result datasets
- [ ] Known limitations and change history

### F. Reagents, standards, and measurement procedure

- [ ] Exact Promega kit catalogue number and manual revision
- [ ] Reagent storage and expiry information
- [ ] λ-DNA supplier, catalogue number, lot, concentration, buffer, and certificate
- [ ] Final sample-to-reagent volume
- [ ] Validated reaction-tube/vial type
- [ ] Pipette ranges and recommended accuracy
- [ ] Tip type and contamination-control method
- [ ] Standard concentration series for 2PT
- [ ] Standard concentration series for MP
- [ ] Dilution calculations and worksheets
- [ ] Incubation time and temperature
- [ ] Mixing method
- [ ] Measurement timing window
- [ ] Tube insertion/orientation procedure
- [ ] Cleaning and disposal procedure
- [ ] Workshop chemical risk assessment and local disposal requirements

### G. Preliminary validation package

- [ ] Approved preliminary-validation protocol
- [ ] Hardware, firmware, calibration-suite, and reagent versions
- [ ] Raw CSV files
- [ ] Sample/standard preparation records
- [ ] Replicate plan
- [ ] Blank results
- [ ] Calibration results
- [ ] Residual plots
- [ ] Precision/repeatability results
- [ ] Recovery/accuracy results
- [ ] LOD and LOQ calculations
- [ ] Working-range assessment
- [ ] Deviations and nonconformities
- [ ] Preliminary conclusions and limitations

### H. Final validation package

- [ ] Predefined acceptance criteria
- [ ] Independent final-validation protocol
- [ ] Sufficient replicate and day/operator coverage
- [ ] Between-device assessment if multiple instruments are available
- [ ] Between-day precision
- [ ] Calibration stability/recalibration interval
- [ ] Recovery across the range
- [ ] Interference or matrix assessment where relevant
- [ ] Comparison with a reference fluorometer
- [ ] Locked raw data and reproducible analysis
- [ ] Approved final validation report
- [ ] Formal statement of validated scope

### I. Figures, photographs, and diagrams

- [ ] Cover image
- [ ] Complete-system labelled photograph
- [ ] Functional block diagram
- [ ] Optical-path diagram
- [ ] Electrical/wiring diagram
- [ ] PCB overview
- [ ] Exploded assembly diagram
- [ ] Step-by-step assembly photographs
- [ ] Filter-orientation diagram
- [ ] Tube-orientation diagram
- [ ] PyBadge button-layout diagram
- [ ] UI screenshots
- [ ] Software installation screenshots
- [ ] Calibration Suite screenshots
- [ ] Calibration curve and residual examples
- [ ] LOD/LOQ explanatory diagram
- [ ] Validation-result figures
- [ ] Comparison chart
- [ ] Troubleshooting decision tree
- [ ] Alt text, caption, source, author, date, and license for every figure

### J. Comparison-system evidence

- [ ] Current, dated specification sources for each instrument
- [ ] Acquisition prices with currency, country, tax/shipping basis, and date
- [ ] Reagent and sample-volume information
- [ ] Calibration capabilities
- [ ] Sensitivity and measurement range
- [ ] LOD/LOQ definitions and comparability caveats
- [ ] Portability and power requirements
- [ ] Repairability and availability of design files
- [ ] Open-source license information
- [ ] Teaching, workshop, field, and research suitability criteria
- [ ] Clear separation between manufacturer claims and independent measurements

### K. References and standards

- [ ] Promega QuantiFluor® ONE dsDNA technical manual
- [ ] Promega Quantus™ Fluorometer operating manual
- [ ] ioRodeo Open Colorimeter Plus documentation
- [ ] ioRodeo DNA quantitation documentation
- [ ] DIYNAFLUOR repository, build instructions, BOM, license, and publication
- [ ] Licensed DIN 38402-51:2017-05 copy
- [ ] Licensed DIN 32645:2008-11 copy or confirmed applicable edition
- [ ] Scientific references for fluorescence, calibration, uncertainty, and validation
- [ ] Reference register with access date and evidence type
- [ ] Copyright review: do not reproduce protected standard text, tables, or equations beyond permitted quotation/use

### L. Publication and release engineering

- [ ] Quarto project tested from a clean environment
- [ ] Pinned Quarto and TeX versions
- [ ] A4 template
- [ ] A5 template
- [ ] booklet-imposition instructions
- [ ] fonts and font licenses
- [ ] header/footer design
- [ ] callout design for Safety, Warning, Important, Note, QC, and Troubleshooting
- [ ] print test in colour and grayscale
- [ ] double-sided print test
- [ ] PDF bookmarks and metadata
- [ ] accessible figure alt text
- [ ] release ZIP structure
- [ ] release checksums
- [ ] archived release manifest

## Immediate next content package

The next controlled package should contain:

1. `README.md` first full draft;
2. `metadata/project_metadata.yml` with confirmed author/project data;
3. `metadata/terminology.yml` expanded and approved;
4. `docs/workshop_booklet/chapters/01–04` first drafts;
5. final hardware revision and BOM intake template;
6. firmware/configuration inventory;
7. figure and photograph acquisition plan.
