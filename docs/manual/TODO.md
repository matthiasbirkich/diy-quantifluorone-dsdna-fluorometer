# Manual revision tasks

## Deferred until the instrument is available

- [ ] **BUILD-01 Confirm the fastener schedule.** Deferred by the author on 23 October 2026 because the instrument is not available for inspection. Check screw diameters, lengths, quantities, nuts and washers against the physical joints. Retain existing values as provisional; do not infer a final schedule from photographs. This task does not block editing the software and operating chapters.

| Joint | Existing entry to verify |
|---|---|
| PyBadge cover to enclosure | Four M2.5 x 20 screws with matching nuts |
| Optical module to enclosure | Four M3 x 20 screws with matching nuts |
| Emission housing C | Two M2 x 6 screws with matching nuts |
| Excitation housing and LED holder | M3 x 35 and M3 x 40; exact assignment and quantities unresolved |

## Remaining build documentation

- [ ] Confirm the LED-board supply connection, adapter pin correspondence and actual multiplexer ports.
- [ ] Record accepted print settings and complete the missing assembly illustrations.

## Next editing stage

- [x] Draft chapters 1–3 covering instrument overview, laboratory safety and measurement principles; Word review excerpt prepared.

- [x] Verify software installation instructions against the supplied firmware archive and runtime files; chapters 6 and 7 drafted and checked against source.
- [ ] Confirm the documented installation and file-persistence checks on the physical PyBadge.
- [x] Draft startup, calibration, routine analysis and quality control chapters against the supplied documents and RC2 source; author review and physical checks remain pending.
- [ ] **SW-02 Optional development task: complete and verify the RC2 multipoint export workflow.** Suite v7.3 scientific JSON does not match RC2 model labels or field names. The older v7.2 scientific export omits dilution/range/status metadata. Supply a verified exporter or conversion step before claiming direct Suite-to-device compatibility; preserve the firmware archive unchanged. This is not required for routine two-point sample analysis or off-device characterization in the Calibration Suite.
- [x] Draft chapters 13 and 14 with SYBR Safe optical assessment, separate preparation and calibration, and consolidated references.
- [ ] Verify SYBR Safe on the actual instrument before routine use; the chapter is a literature-based transfer procedure.

## Confirmed measurement workflow

Routine: 1 µL DNA-containing sample plus 200 µL ONE reagent, measured against the two-point calibration. Initial characterization: evaluate a multipoint series in the Calibration Suite for each new instrument or configuration; retain regression and performance statistics. Provisional calibration data are not required for routine sample batches.

- [x] Draft chapters 11 and 12 on performance, limitations, maintenance and troubleshooting.
