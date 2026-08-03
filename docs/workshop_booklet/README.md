# Workshop booklet and PDF generation

This directory contains the canonical **Quarto book project** for the workshop booklet.

## Source-of-truth rule

- Files under `docs/workshop_booklet/` are the editable source of truth.
- Files under `docs/markdown/` are synchronized Markdown reading copies.
- Do not edit the Markdown copy independently and then expect the QMD source to update.
- Only files listed in `_quarto.yml` are part of the active booklet.

## Active structure

1. Introduction and Learning Objectives
2. Safety and Laboratory Requirements
3. Theory and References
4. Hardware and Assembly
5. Getting Started: Basic Operation and Menu Navigation
6. Calibration Suite and Data Transfer
7. Software Installation
8. Measurement Protocol
9. Calibration, Results, and Quality Control
10. Validation and Performance
11. Troubleshooting
12. Workshop Exercises and Checklists
13. References

Appendices are stored under `appendices/`.

The former 25-chapter placeholder scaffold is preserved under:

`archive/legacy_25_chapter_scaffold/`

It is retained for traceability and is not rendered.

## Render commands

From `docs/workshop_booklet/` run:

```bash
quarto render
```

To render only HTML:

```bash
quarto render --to html
```

To render only PDF:

```bash
quarto render --to pdf
```

Quarto writes the output to `_book/`.

## Editing workflow

1. Edit the relevant `.qmd` file.
2. Keep the chapter title in YAML front matter; do not add a duplicate numbered H1 heading.
3. Use `##` for main sections and `###` for subsections.
4. Add or remove active chapters only by editing `_quarto.yml` at the same time.
5. Regenerate the corresponding Markdown copy under `docs/markdown/`.
6. Render and review HTML before PDF.
7. Commit source, synchronized Markdown, and configuration changes together.
