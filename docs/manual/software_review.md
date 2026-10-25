# Software and operation review

Date: 23 October 2026. Source: the preserved `QuantiFluorONE_Firmware_1.0.0-rc2-stable.zip` from repository baseline `e9de6b394860beec91f53efd38cc55459f0cb216`.

## Evidence and method

Read `boot.py`, `code.py`, `quantifluorone_app.py`, `src/constants.py`, configuration and saved calibration/state JSON directly from the ZIP. Inspected the reset-access, bootloader, reload and control photographs. Compared all four software binaries/archive files against `software/SHA256SUMS.txt`. The application archive is unchanged.

The documentation review does not run CircuitPython on the PyBadge and does not establish physical button timing, USB ownership on a particular host, sensor behavior or instrument write persistence. These need the installation checks described in the manual.

## Findings incorporated in chapters 6 and 7

| Topic | Source evidence | Documentation consequence |
|---|---|---|
| Application identity | `VERSION` is RC2; bundled configuration and saved model contain RC1 metadata | Identify executable version by application/banner and preserved release checksum |
| Bundled calibration | Enabled provisional multipoint model plus historical blank/state and logs | Keep the ZIP unchanged; remove historical calibration/state from a new device installation before analytical use |
| Provisional import | Import checks mathematical fields but does not reject PROVISIONAL | Operator must verify analytical suitability; import success is not approval |
| New blank after two-point calibration | `measure_blank` disables the model and attempts to delete its file | Do not press START as a routine preliminary step when reusing stored two-point calibration |
| Stored blank check | A performs a sample acquisition without replacing blank state | A traceable blank-check tube can be measured with A and evaluated in the QC procedure |
| Sample list selection | `samples.list` is read; `sample_index` comes from state | Remove the unsupported `samples.selected_index` example from the new instructions |
| Sample ID escaping | CSV strings are written with comma separators without quoting | Avoid commas, quotation marks and line breaks in sample IDs |
| Controls | Constants plus event dispatcher | SELECT opens the menu from Live; UP/DOWN sample selection is Live only; A/B do not change sensor gain/time |
| Calibration review | `candidate_qc` warns; save still possible | Investigate CV/SNR/SAT; ACTIVE does not constitute independent QC acceptance |
| Calibration identification | ID is read/stored but not displayed in status pages | Verify calibration identity from archived JSON and batch record |
| Logging time | `time.monotonic()` populates `t_s` | Document batch date and restart boundaries separately; no UTC claim |
| Logging persistence | `_log` catches errors; Live screen omits general status | Verify actual CSV rows after installation; a displayed result does not prove saving |
| Direct sensor fallback | Enabled by configuration; channel -1 | Treat direct topology as a departure from the documented multiplexer build |
| Safe-mode picture | Existing file shows reload/soft reboot | Omit it as a claimed safe-mode confirmation |

## Changes prepared

- Added source-based installation and startup/operation chapters under `docs/manual/chapters`.
- Added notices to legacy installation and basic-operation chapters pending their complete migration.
- Corrected the broken installation link in `software/README.md`.
- Extended the Word excerpt builder to select chapter groups while retaining Quarto text as the source.
- Deferred fastener inspection remains BUILD-01 and does not block this stage.

## Follow-up

An additional review of the calibration suites found that v7.3 scientific JSON is not directly RC2-compatible: the model is labelled `OLS linear` and uses `mean_reference` / `sxx_reference2`, while RC2 accepts `OLS` and reads `mean_concentration` / `sxx_concentration2` with the two-sided t factor inside `multipoint`. The v7.2 scientific JSON has the mathematical shape but does not supply operational dilution/range/status metadata. The separate v7.2 configuration export targets DIYNAFLUOR rather than this application. This is tracked as SW-02.

An isolated execution of the original RC2 import method with synthetic schema fixtures confirmed rejection of the v7.3 field shape, rejection after changing only its model label, and a dilution-factor default of 1 for otherwise valid input without that field. This is a software-contract check, not analytical validation or a device test.

- Verify the power, storage and restart procedure on the physical instrument.
- Make the later calibration and routine-measurement chapters consistent with the confirmed START behavior.
- Distinguish blank-check measurements from replacement of the calibration blank throughout the book.
- Retain firmware behavior as documented; any change to that behavior is a separate software revision with its own verification.

The public repository and preserved firmware archive have not been changed by this review.

## Output verification

All four software checksum entries matched. All 41 local file/image links across the four drafted chapters resolved. The final Word excerpt for chapters 6 and 7 was rendered and all eight pages were inspected; table rows remain intact at page breaks. Hardware verification remains pending.

## Calibration and routine-analysis excerpt

Chapters 8, 9 and 10 now distinguish the TM405 single-tube reagent blank (200 microlitres, no DNA addition), the 201-microlitre DNA assay, stored two-point blank checks, independent QC, predilution and the actual CSV semantics. The final nine-page Word excerpt was rendered and every page inspected. All 45 relative resource links across the seven drafted chapters resolve locally; the firmware ZIP checksum remains unchanged. The Suite v7.3 direct-export gap remains open as SW-02.

## Author clarification on routine operation

Routine analysis uses 1 µL DNA-containing sample plus 200 µL ONE reagent and the two-point calibration. A multipoint series evaluated in the Calibration Suite is used for initial characterization of each new device or configuration. It is not a recurring batch step and does not require importing the provisional model for routine work. SW-02 concerns optional multipoint import only and is not a blocker for characterization or routine analysis. Chapters 8–10 have been revised accordingly. Earlier Word excerpts predate this clarification and require regeneration before the next delivery.
