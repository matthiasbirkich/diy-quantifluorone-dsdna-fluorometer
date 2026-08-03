# Workshop booklet and PDF generation

This directory contains a **Quarto book project**.

## Contents

- `_quarto.yml` — booklet configuration
- `index.qmd` — booklet landing page
- `chapters/` — individual chapters in Quarto Markdown format

## Prerequisites

1. Install **Quarto**
2. Install a PDF engine
   - easiest option: **TinyTeX**
   - alternatives: TeX Live or MiKTeX

## Render commands

From this directory run:

```bash
quarto render
```

This renders both HTML and PDF outputs as configured in `_quarto.yml`.

To render only HTML:

```bash
quarto render --to html
```

To render only PDF:

```bash
quarto render --to pdf
```

## Expected output

Quarto creates an output directory such as `_book/` that contains the rendered
booklet files.

## Suggested workflow

1. update or add chapter `.qmd` files;
2. place referenced figures in `docs/figures/`;
3. run `quarto render`;
4. review the HTML output first;
5. review and adjust the PDF output;
6. commit both source files and, if desired, the generated PDF.


## Software-installation chapter

Chapter 07 distinguishes normal restart, **slow-double-click safe mode**, and
fast-double-click UF2 bootloader mode. This distinction is essential when
managing firmware, CSV, and JSON files on the QuantiFluorONE PyBadge.
