# Standards register

| Standard | Edition cited | Scope |
|---|---|---|
| DIN 38402-51 | 2017-05 | Linear calibration and assessment of the calibration function |
| DIN 32645 | 2008-11 | Decision, detection and determination limits under repeatability conditions |

These are the editions referenced by the project. Formal conformity requires
review against the applicable licensed standard, not merely a software self-test.

## Instrument screening estimates

The shipped ONE configuration uses LOD = 3.3 × blank SD / slope and
LOQ = 10 × blank SD / slope, based on ten independent reagent-blank tubes.
These are screening estimates, distinct from a calibration-curve assessment.

## Calibration Suite v7.3

The OLS calculation distinguishes NWG, EG and BG, records alpha, k and the
number of future determinations, and includes an embedded openDIN self-test.
DIN-labelled limits and OLS uncertainty bands are suppressed for weighted
models. See the [audit notes](../../software/calibration_suite/V7.3_STANDARDS_AUDIT_NOTES.md)
and [calibration chapter](../manual/chapters/08_calibration.qmd).

The on-device two-point method remains the routine measurement route.
v7.3 scientific JSON is not directly compatible with the RC2 importer.
