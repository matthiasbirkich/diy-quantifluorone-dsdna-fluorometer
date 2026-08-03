# DIY-QuantiFluorONE-dsDNA-Fluorometer — push overlay v6

This update resolves the conflict between the developed booklet chapters and the former 25-chapter placeholder scaffold.

## Canonical result

- one active Quarto booklet;
- 13 numbered chapters plus appendices;
- no duplicate active chapter numbers;
- QMD files as the editorial source of truth;
- synchronized Markdown reading copies;
- the complete old placeholder scaffold retained in an archive directory for traceability.

## Main files to review

- `docs/workshop_booklet/_quarto.yml`
- `docs/workshop_booklet/STRUCTURE.md`
- `docs/workshop_booklet/chapters/08_measurement_protocol.qmd`
- `docs/workshop_booklet/archive/legacy_25_chapter_scaffold/README.md`
- `docs/markdown/index.md`

Suggested commit message:

```text
docs(booklet): consolidate workshop booklet structure and add measurement protocol
```
