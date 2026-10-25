# Build review

Inspected baseline: `e9de6b394860beec91f53efd38cc55459f0cb216`.
Review date: 23 October 2026.

## Completed checks

- Inspected eight photographs/CAD views directly, including the loose LED board, exposed emission filter and mounted detector. Avoided reusing the misleading excitation-side caption.
- Imported the ten genuine mechanical STEP files using OpenCascade through CadQuery. Each imported as one solid. This does not establish geometric validity or assembly fit.
- Parsed all seven STL files as binary triangle meshes. Their byte counts match their declared triangle counts.
- Compared the overall STEP and STL dimensions for all seven optical pairs. Sorted axis lengths agree within 0.01 mm. This is not a surface equivalence test.
- Located the genuine B STEP file in `hardware/mechanical/stl/`. The original file at the expected STEP path was an Apple binary property-list reference, not CAD data. Replaced that invalid file with an exact copy of the genuine STEP; retained the genuine source at its original path for now.
- Inspected the LED fabrication ZIP: Gerber layers and plated/non-plated drill files are present.
- Corrected the obsolete reusable hardware description from an SMD rev2 addressed LED board to the documented fixed-current radial rev3 board.
- Wrote two Quarto chapters and an explicit file index. Existing published manual sources remain in their original location until the full book is migrated.

- Verified every relative resource link in both QMD chapters resolves in the local repository.
- Rendered the Word excerpt and visually checked all seven pages after correcting the initial table export. Tables and hyperlinks remain editable Word content.

## Author questions needed to finish the build instructions

1. Resolved on 23 October 2026: the author confirms `E_LED Board + Vial Halter.step` as the installed standard. It has no corresponding combined-holder STL in the inspected directory. The thin and alternative versions remain alternatives.
2. Deferred by the author on 23 October 2026 until the instrument is available: confirm the optical-module fasteners and their joints. Existing values remain provisional. The existing BOM covers enclosure fasteners only; older text additionally lists M2 x 6, M3 x 35 and M3 x 40 and assigns M3 x 40 more than once. Track this as BUILD-01 in [TODO.md](TODO.md); it does not block further chapter editing.
3. Confirm the actual LED-board connection, downstream port choices and PyBadge/PRT-15109 adapter pin correspondence. Existing wiring records explicitly leave parts of this unresolved.

## Illustration discrepancies

- `pybadge_enclosure_cad.jpeg` primarily depicts the optical module rather than an isolated controller enclosure. Omitted from the controller installation instructions.
- `light_shield_part_cad.jpeg` depicts a small housing rather than an unambiguous view of the large F cover. Omitted from the cover installation instructions.
- `iorodeo_radial_16mA_assembly.png` labels U1 as TPS61200, whereas the supplied KiCad schematic identifies TPS61222DCK; other electrical labels also require reconciliation. It is not used as an authoritative assembly drawing in the new chapters.

## Further items for the next editing pass

- Record the accepted print material, orientation, layer height, infill and support strategy.
- Decide whether enclosure and controller-cover STL exports should be added after confirmation of the STEP models.
- Obtain or identify a clear excitation-filter installation photograph. Existing filenames and captions do not establish a complete photographic sequence.
- Reconcile the cable count and optional battery capacity across the BOM and old chapter.
- Match supplied KiCad sources to the revision-specific fabrication package before describing them as a fabrication-verified set.
- Check upstream mechanical attribution and applicable licences for each adapted design.
- Check stored wiring illustrations against the confirmed electrical topology before including them in the new chapter.

No remote commits, tag publication or release have been made during this editing step.

## Manufacturer standard reconciliation

The newly supplied TM405 ONE manual specifies 400 micrograms/mL, equivalent to 400 ng/microlitre; 1 microlitre contributes 400 ng DNA to 200 microlitres reagent. The separate QuantiFluor dsDNA protocol specifies 100 micrograms/mL, equivalent to 100 ng/microlitre; its recommended standard adds 2 microlitres, contributing 200 ng. The Quantus handbook lists both separately. Confirm the bottle and standard actually used before changing calibration values or performance claims.

The author has confirmed that the bottle actually used is QuantiFluor ONE Lambda DNA, 400 µg/mL. The stock concentration is therefore 400 ng/µL; the documented 1 µL aliquot contributes 400 ng DNA. The 400 ng/µL calibration anchor remains appropriate on the original-sample basis for this preparation; no factor-of-four correction is indicated by this clarification. Corrected the erroneous µg/µL quick-start wording in both the existing Quarto and Markdown chapters and distinguished stock concentration, DNA mass and in-assay concentration.
