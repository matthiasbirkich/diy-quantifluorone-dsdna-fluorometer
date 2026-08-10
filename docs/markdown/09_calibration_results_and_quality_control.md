---
document-status: "Current"
validation-status: "Validated configuration"
date: "2026-08-10"
---

# 09 — Calibration, Results, and Quality Control

> **Scope:** This chapter provides the concise operational workflow for routine laboratory decisions. The theoretical and statistical basis of calibration, prediction intervals, LOD, and LOQ is described in Chapter 3.

## Calibration routes

Use one of the following calibration routes before measuring unknown samples.

| Calibration route | Preparation and evaluation | Instrument action | Appropriate use |
|---|---|---|---|
| On-instrument two-point calibration | Blank and one known standard | `SELECT → 2-PT CAL` | Rapid routine measurements within a limited working range |
| Multipoint calibration | Evaluate calibration CSV data in the Open Fluorometer Calibration Suite v7.2 Stable | Copy the accepted firmware-compatible JSON to `CIRCUITPY`, then use `SELECT → LOAD MP CAL` | Measurements requiring a defined calibration range, prediction error, LOD, LOQ, and documented model checks |
| Stored calibration | Review the stored calibration identity and status | `SELECT → CAL STATUS` | Continued work under unchanged and verified conditions |
| No valid calibration | Raw-signal inspection only | Do not report a concentration | Instrument checks and troubleshooting |

A calibration that loads successfully is not automatically suitable for the current samples.

## Use the Calibration Suite

The Calibration Suite is the primary tool for creating, evaluating, documenting, and exporting a multipoint calibration.

### Prepare the calibration dataset

Use standards prepared with the same:

- QuantiFluor® ONE dsDNA chemistry;
- sample and reagent volumes;
- tube type;
- incubation conditions;
- instrument configuration;
- gain and integration settings; and
- concentration basis intended for the unknown samples.

Import the calibration CSV into the Calibration Suite and confirm that the analytical-signal and reference-value columns were identified correctly.

For the standard assay described in Chapter 8, each tube contains:

- 1 µL standard or sample; and
- 200 µL QuantiFluor® ONE reagent.

The total assay volume is 201 µL.

### Evaluate the calibration

In the Calibration Suite:

1. Enter a unique calibration ID and the calibration date.
2. Confirm the reference-value basis and concentration unit.
3. Calculate the intended calibration model.
4. Inspect the calibration curve and residual plot.
5. Review replicate precision, recovery, outlier flags, and range coverage.
6. Review the slope, intercept, residual error, LOD, LOQ, and prediction statistics.
7. Confirm that no systematic trend, unexplained outlier, or unsuitable range remains.
8. Save or print the calibration report.

Do not accept a calibration from the coefficient of determination alone. A high \(R^2\) does not compensate for degraded standards, poor pipetting, an unsuitable range, or systematic residuals.

The current QF1-1.0.0-rc2 firmware imports an OLS multipoint calibration. Do not load another model type unless the firmware release documentation explicitly confirms compatibility.

### Export the operational calibration

After the model has been accepted:

1. Export the firmware-compatible calibration JSON from the Calibration Suite.
2. Save the accepted file as:

   ```text
   quantifluorone_multipoint.json
   ```

3. Retain the original CSV, Calibration Suite report, and exported JSON together.
4. Do not edit individual coefficients manually after export.

The Calibration Suite report is the complete calibration record. The JSON file is the operational copy used by the fluorometer.

## Load and verify a multipoint calibration

To transfer an accepted multipoint calibration:

1. Connect the switched-on instrument to a computer with a USB data cable.
2. Make `CIRCUITPY` writable from the computer as described in Chapter 7.
3. Copy `quantifluorone_multipoint.json` to the root of `CIRCUITPY`.
4. Replace the previous file only when the new calibration has been checked and archived.
5. Safely eject and disconnect `CIRCUITPY`.
6. Power the instrument from its normal standalone power source.
7. Open `SELECT → LOAD MP CAL`.
8. Confirm the import.
9. Open `SELECT → CAL STATUS`.

Check at least:

- calibration ID;
- calibration type;
- calibration status;
- calibration range;
- concentration basis and unit;
- LOD and LOQ; and
- availability of the prediction error.

Measure and store a fresh reagent blank after loading a new calibration.

> Loading a new JSON does not replace the need for a current blank and passing QC samples.

## Check calibration validity before each batch

Use a stored or imported calibration only when all of the following are true:

- the calibration status is acceptable for the intended work;
- the calibration ID and date are documented;
- the assay, tube type, volumes, and concentration unit match;
- the instrument hardware and optical configuration are unchanged;
- the gain, integration time, and signal definition match;
- the standards and samples use the same concentration basis;
- the expected sample concentrations are covered by the calibration range;
- the calibration slope is positive;
- required LOD, LOQ, range, and error fields are available; and
- the laboratory-defined validity period has not expired.

Reject or replace the calibration when:

- the wrong file, assay, unit, or concentration basis was selected;
- required fields are missing;
- the expected samples fall outside the validated range;
- the instrument, optical holder, LED, filter, or sensor configuration has changed;
- reagent or standards are known to be degraded; or
- QC performance no longer supports the calibration.

## Measurement-batch sequence

Use the following sequence for each batch:

1. Confirm the active calibration under `CAL STATUS`.
2. Measure a fresh reagent blank.
3. Measure at least one independent QC sample.
4. Measure the unknown samples.
5. Repeat QC after a long interruption, suspected drift, or instrument change.
6. Measure a final QC sample when required by the laboratory procedure.
7. Review the complete batch before accepting results.

For a broad calibration range, preferably use low-, mid-, and high-level QC samples. QC material should be independent of the standards used to create the calibration whenever suitable material is available.

## Evaluate replicate measurements

### Three readings within one measurement cycle

The fluorometer uses three TSL2591 readings to calculate one measurement-cycle mean and standard deviation.

These are technical sensor repeats. They are not three independently prepared assays.

Check for:

- an unusually large standard deviation;
- a progressive increase or decrease;
- bubbles in the optical path;
- incomplete mixing;
- incorrect tube seating or orientation;
- fingerprints, droplets, or contamination on the tube; and
- movement or stray-light entry during measurement.

When a visible technical cause is present:

1. correct the problem;
2. remix gently when appropriate;
3. allow bubbles to disappear;
4. reposition or replace the tube; and
5. repeat the measurement.

Do not delete an individual reading without recording a technical reason.

### Independently prepared assay replicates

Independent replicates require separate pipetting of sample and reagent.

When replicate concentrations disagree:

1. check sample identity, calculations, pipetting, mixing, incubation, and tube placement;
2. remeasure the existing tubes;
3. prepare fresh independent replicates if disagreement remains; and
4. reject the result when no reproducible value can be obtained.

Near zero concentration, relative standard deviation may be misleading. Evaluate the absolute spread together with LOD and LOQ.

## Evaluate blank and QC samples

### Reagent blank

The blank must:

- use the same reagent and vessel type as the samples;
- contain no intentionally added dsDNA;
- be prepared and incubated with the batch; and
- remain within the laboratory-defined blank acceptance criterion.

An elevated or unstable blank may indicate contamination, carryover, bubbles, degraded reagent, an unsuitable calibration, or an optical problem.

When the blank fails:

1. prepare and measure a fresh blank;
2. inspect reagent, tubes, pipettes, and the optical chamber;
3. replace contaminated or degraded materials; and
4. repeat the calibration or affected batch when necessary.

Do not use a clearly invalid blank to correct unknown samples.

### Quality-control samples

A QC sample passes only when its result lies within a predefined acceptance interval.

The interval must be established before reviewing the batch and may be based on:

- an independently assigned target value;
- historical control data;
- an approved recovery range; or
- another documented laboratory criterion.

Do not create or widen QC limits after seeing the result.

When QC fails:

1. stop accepting unknown-sample results;
2. check the calibration, blank, dilution, pipetting, mixing, reagent, and tube placement;
3. repeat the QC measurement after correcting an identified technical problem;
4. prepare a fresh QC assay when required; and
5. repeat affected unknown samples if QC performance cannot be restored.

Results measured since the last passing QC sample are potentially invalid.

## Interpret concentration, prediction error, LOD, and LOQ

### Concentration basis

The current firmware reports the principal concentration on the original-sample basis defined by the calibration. The corresponding in-assay concentration may also be retained in the CSV output.

Do not mix original-sample and in-assay values.

The normal assay dilution caused by adding 1 µL sample to 200 µL reagent is already represented by the calibration metadata. Do not multiply the displayed original-sample result by 201.

Apply an additional factor only when the original unknown sample was deliberately diluted before assay preparation:

\[
c_\text{original}=c_\text{reported}\times F_\text{pre-dilution}
\]

Record the pre-dilution factor.

### Prediction error

For an imported multipoint calibration, the displayed `95% PI +/-` value is the half-width of the two-sided prediction interval for one analytical determination.

It is not the same as:

- the standard deviation of the three sensor readings;
- variation between independently prepared replicates; or
- uncertainty introduced by a manual pre-dilution.

Report concentration with its prediction error only when:

- a valid multipoint calibration is active;
- the prediction interval is available;
- the result lies within the calibration range;
- the result is at or above the LOQ; and
- blank, QC, and replicate criteria have passed.

### LOD and LOQ

Use the LOD and LOQ belonging to the active calibration and confirm their concentration basis.

| Result | Interpretation | Reporting action |
|---|---|---|
| Below LOD | The signal cannot be distinguished reliably from the blank | Report `< LOD` or `not detected`, according to the laboratory procedure |
| At or above LOD but below LOQ | dsDNA may be detected, but the concentration is not reliably quantifiable | Report `< LOQ` or `detected, not quantified` |
| At or above LOQ and within range | The result may be quantified if all other criteria pass | Report concentration and prediction error where available |
| Above the upper calibration limit | The result is outside the validated range | Dilute the original sample and repeat the complete assay |
| Below the lower validated range | The numerical estimate is outside the validated range | Do not report it as a normal quantitative result |

Negative blank-corrected values must not be reported as negative dsDNA concentrations. Report them according to the laboratory procedure, normally as `< LOD`.

## Accept, repeat, dilute, or reject

| Observation | Decision | Required action |
|---|---|---|
| Calibration valid; blank and QC pass; replicates agree; result at or above LOQ and within range | **Accept** | Report the result and record any pre-dilution |
| One tube shows unstable readings, bubbles, contamination, or incorrect placement | **Repeat measurement** | Correct the technical problem and remeasure the same tube |
| Independent assay replicates remain inconsistent | **Repeat assay preparation** | Prepare fresh independent replicates |
| Calibration is incompatible, expired, or incomplete | **Reject** | Load or create an acceptable calibration |
| Result is above range or the detector response is saturated | **Dilute and repeat** | Dilute the original sample, repeat the complete assay, and apply the recorded pre-dilution factor |
| Result is below LOQ | **Do not accept as a normal quantitative result** | Report according to the LOD/LOQ category |
| Blank fails | **Hold the batch** | Investigate and obtain an acceptable blank |
| QC fails | **Hold or reject affected results** | Correct the cause and repeat QC and affected samples |
| Wrong sample, dilution, reagent, protocol, unit, or calibration was used | **Reject** | Repeat the assay correctly |
| No technically justified and reproducible result can be obtained | **Reject** | Record the result as invalid and document the reason |

## Minimum documentation

Record at least:

- date and operator;
- instrument and firmware version;
- Calibration Suite version;
- calibration ID, date, type, status, and range;
- calibration report and operational JSON filename;
- reagent and standard identification;
- blank result;
- QC target, acceptance interval, and result;
- sample identifier;
- individual replicate results;
- measurement-cycle mean and standard deviation;
- prediction error where available;
- LOD and LOQ with concentration basis;
- pre-dilution factor;
- final reported result;
- acceptance decision; and
- reason for every repetition, dilution, exclusion, or rejection.

Retain the original data. Repeated or corrected measurements must not overwrite earlier results without traceability.

## Bench-side checklist

Before reporting a quantitative result, confirm:

- **Accepted calibration active?**
- **Calibration ID and range correct?**
- **Fresh blank passed?**
- **QC passed?**
- **Replicates consistent?**
- **Result at or above LOQ?**
- **Result within the calibration range?**
- **Prediction error available when required?**
- **Pre-dilution recorded?**
- **No unresolved technical fault?**

Only when all applicable checks pass may the result be accepted as quantitative.
---

⬅️ Previous Chapter: [Measurement Protocol](08_measurement_protocol.md)

📖 [Documentation Summary](SUMMARY.md)

➡️ Next Chapter: [Validation and Analytical Performance](10_validation_and_analytical_performance.md)
