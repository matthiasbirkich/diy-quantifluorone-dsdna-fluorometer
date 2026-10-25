# Assembly and Operating Manual

The authoritative text is the fourteen numbered `.qmd` files in `chapters/`.
English is used for the manual. Quarto metadata and navigation are in `_quarto.yml`
and `index.qmd`. The text includes the preassembled LED-board option in Chapter 4.

## Current manual

Author: Dipl.-Ing. Matthias Birkicht, Centre for Tropical Marine Research.
The edition dated 24 October 2026 contains 45 pages and fourteen chapters.

- [Complete manual PDF](downloads/DIY_QuantiFluorONE_Manual.pdf)
- [Editable manual Word](downloads/DIY_QuantiFluorONE_Manual.docx)
- [Launch Calibration Suite v7.3](https://matthiasbirkich.github.io/diy-quantifluorone-dsdna-fluorometer/software/calibration_suite/Open_Fluorometer_Calibration_Suite_v7.3.html)

## Chapters

- [1 Instrument Overview and Intended Use](chapters/01_instrument_overview.qmd)
- [2 Safety and Laboratory Requirements](chapters/02_safety.qmd)
- [3 Measurement Principles](chapters/03_measurement_principles.qmd)
- [4 Components Tools and Reproduction Files](chapters/04_components_and_files.qmd)
- [5 Instrument Assembly](chapters/05_assembly.qmd)
- [6 Software Installation and Updates](chapters/06_software_installation.qmd)
- [7 First Startup and Instrument Operation](chapters/07_startup_and_controls.qmd)
- [8 Calibration and Calibration Management](chapters/08_calibration.qmd)
- [9 Routine dsDNA Analysis with QuantiFluor ONE](chapters/09_routine_analysis.qmd)
- [10 Results Quality Control and Data Management](chapters/10_results_and_qc.qmd)
- [11 Analytical Performance and Limitations](chapters/11_performance.qmd)
- [12 Maintenance and Troubleshooting](chapters/12_maintenance_and_troubleshooting.qmd)
- [13 Alternative Assay with SYBR Safe](chapters/13_sybr_safe.qmd)
- [14 References Design Sources and Acknowledgements](chapters/14_references.qmd)

These QMD chapters are authoritative. Intermediate renders and individual chapter
drafts in review/ are excluded from publication. After rendering and checking the
complete edition, update both stable files in downloads/ before publication.

## Rendering

Quarto 1.9.38 was used to check the full book configuration. HTML can be built with:

```sh
quarto render docs/manual --to html
```

The portable Word review renderer reads the same QMD files directly. It avoids
an observed table-import problem between the Quarto/Pandoc Word export and the
headless LibreOffice renderer used for review. There is no separate edited Word
text source. Python requires python-docx; the final pagination pass also uses
PyMuPDF. Use the established A4 manual format.

```sh
python docs/manual/render_review.py --book
python docs/manual/finalize_docx.py
python render_docx.py docs/manual/review/DIY_QuantiFluorONE_Assembly_and_Operating_Manual.docx --output_dir /path/to/qa --emit_pdf
python docs/manual/finalize_docx.py --pagination-pdf /path/to/qa/DIY_QuantiFluorONE_Assembly_and_Operating_Manual.pdf
python render_docx.py docs/manual/review/DIY_QuantiFluorONE_Assembly_and_Operating_Manual.docx --output_dir /path/to/final-qa --emit_pdf
```

`render_docx.py` refers to the document renderer available in the authoring
environment. A local LibreOffice export to PDF can supply the pagination PDF
instead. After the last export, verify that chapter start pages match the
contents and copy the checked PDF to the review directory. The contents links
and page numbers are regenerated during this build; regenerate them after edits.

For the separate new-chapter excerpt:

```sh
python docs/manual/render_review.py --chapters 13 14
```

Inspect every rendered page before releasing a Word or PDF edition. Do not
release `review/manual_source.docx` or an unchecked direct Quarto Word export.

## Outstanding verification

The screw schedule remains deferred until physical inspection. Cable supply and
adapter connections, print settings and device installation checks remain in
`TODO.md` and the review registers. SYBR Safe is a literature-based transfer
procedure and has not been qualified on the actual instrument. The optional
multipoint import limitation does not block routine two-point operation.

Repository file links in the portable editions point to GitHub main. Newly added
manual files and corrected filenames need to be published there with the agreed
repository revision before all such links are publicly available. No public
repository change is made by rendering these review editions.
