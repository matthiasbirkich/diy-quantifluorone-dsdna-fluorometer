# QuantiFluorONE Theory and References — Repository Patch

**Patch date:** 2026-08-02  
**Content language:** English  
**Purpose:** Add a concise, workshop-oriented theory chapter and the supporting reference files.

## Included files

```text
docs/
├── workshop_booklet/chapters/03_theory_and_references.qmd
├── markdown/03_theory_and_references.md
├── source_files/content/hardware_configuration.md
├── figures/source/
│   ├── qfo_ex470bp40_spectral_verification.jpeg
│   ├── qfo_em532bp40_spectral_verification.jpeg
│   └── filter_spectral_verification_README.md
└── references/
    ├── references.bib
    ├── standards_register.md
    └── source_register.csv
patches/
└── README_optical_architecture.patch
```

## What this patch does

- Adds the practical theory needed for the dsDNA workshop activity without turning the booklet into a fluorescence textbook.
- Defines the final one-sensor optical path at 90°.
- Records the installed LED, filters, Promega E4941 tubes, TSL2591, PCA9546, PyBadge, and cabling.
- Separates supplier filter specifications from the project’s independent spectral verification.
- Summarizes blank correction, two-point and multipoint calibration, and the LOD/LOQ procedures implemented in the firmware and Calibration Suite 7.2 Stable.
- Adds consistent references and a standards register.
- Provides a small README patch replacing “approximately 90°” with “at 90°”.

## Integration

Extract this archive at the repository root. Review the README diff, then apply it manually or with Git:

```bash
git apply patches/README_optical_architecture.patch
git add docs patches/README_optical_architecture.patch
git commit -m "Add practical theory and references chapter"
```

The Markdown file is included for immediate GitHub use. The Quarto file is the editable booklet source.

## Deliberate scope limit

The chapter contains only the theory needed to build confidence in the practical workflow. Detailed derivations, full standards commentary, and publication-level validation reports remain outside the workshop chapter and can be added later under `validation/` and `docs/references/`.
