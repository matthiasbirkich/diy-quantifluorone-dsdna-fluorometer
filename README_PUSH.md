# Booklet-structure cleanup push package

This repository state is prepared for review in Working Copy.

## What changed

The old 25-chapter placeholder scaffold has been archived, while the active Quarto project now contains 13 chapters plus appendices. Developed content was retained, canonical filenames were assigned, and Chapter 08 was added from the supplied Measurement Protocol.

## Before committing

1. Review `docs/workshop_booklet/STRUCTURE.md`.
2. Open `docs/workshop_booklet/_quarto.yml` and confirm the chapter order.
3. Confirm that `docs/workshop_booklet/chapters/` contains no duplicate active chapter numbers.
4. Confirm that the legacy files are present only under `docs/workshop_booklet/archive/legacy_25_chapter_scaffold/`.
5. Review Chapter 08 and the synchronized `docs/markdown/08_measurement_protocol.md`.
6. Commit the complete change as one conceptual documentation update.

Suggested commit message:

```text
docs(booklet): consolidate structure and add measurement protocol
```
