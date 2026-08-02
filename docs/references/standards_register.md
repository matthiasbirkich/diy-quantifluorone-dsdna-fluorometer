# Standards Register

| Standard | Edition | Use in this repository | Limitation |
|---|---:|---|---|
| DIN 38402-51 | 2017-05 | Reference for linear calibration, calibration design, and interpretation of a linear calibration function | The repository cites the standard but does not reproduce protected text. A licensed copy is required for formal conformity assessment. |
| DIN 32645 | 2008-11 | Reference for decision, detection, and quantification limits under repeatability conditions | Calibration Suite 7.2 Stable documents its multipoint calculation as the indirect calibration-curve method summarized in CLB1. Formal conformity requires a documented code-to-standard review using a licensed copy. |

## Project implementation summary

### Two-point firmware

```text
LOD estimate = 3 × s_blank / slope
LOQ estimate = 10 × s_blank / slope
```

These are blank-based workshop and instrument-evaluation estimates.

### Calibration Suite 7.2 Stable

The suite uses the residual standard deviation, calibration slope and design, Student-t factors, significance level, number of future determinations, and quantification factor `k`. The LOQ is solved iteratively. The software report records the selected settings and calculation description.
