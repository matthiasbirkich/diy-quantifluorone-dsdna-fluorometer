---
document-status: "Current"
validation-status: "Validated configuration"
date:  "2026-08-14"
---

This chapter summarizes the most common operational problems that may occur during assembly, firmware installation, calibration, and routine measurements. It is intended as a practical troubleshooting guide for workshop participants and laboratory users. More detailed background information is provided in the previous chapters.

## Hardware

| Symptom | Possible cause | Recommended action |
|----------|----------------|--------------------|
| Display remains dark | Battery discharged | Recharge the PyBadge or connect USB power. |
| Device does not start | CircuitPython not installed correctly | Repeat the firmware installation (Chapter 5). |
| LED does not illuminate | Loose cable or incorrect connector | Verify all wiring and connector orientation. |
| Sensor not detected | Qwiic/STEMMA cable disconnected or I²C scan unsuccessful | Check the cable, connectors, and I²C connections, then restart the instrument. |
| Very low fluorescence signal | Optical filters installed incorrectly | Verify the orientation and seating of both optical filters. |
| Signal permanently saturated | Light shield open, optical light leak, or excessive sample signal | Close the light shield and inspect the optical path. If the sample remains above range, dilute it and repeat the assay. |

## Firmware and Software

| Symptom | Possible cause | Recommended action |
|----------|----------------|--------------------|
| Calibration cannot be loaded | Missing or incompatible JSON file | Export the calibration again using the Calibration Suite. |
| Calibration import fails | Invalid JSON format | Validate the calibration file before copying it to the device. |
| Device reports "uncalibrated" | No calibration selected | Load a valid calibration before measuring samples. |
| Device freezes during startup | Incomplete firmware installation | Reinstall the firmware according to Chapter 5. |

## Calibration

| Symptom | Possible cause | Recommended action |
|----------|----------------|--------------------|
| Blank values unstable | Ambient light or contaminated PCR tube | Repeat the blank measurement using a clean tube under stable conditions. |
| Calibration rejected | Standards prepared incorrectly | Prepare fresh standards and repeat the calibration. |
| Unknown outside calibration range | Sample concentration exceeds the validated range | Dilute the sample and repeat the measurement. |
| High calibration uncertainty | Pipetting errors or degraded standards | Prepare fresh standards and recalibrate. |

## Measurement

| Symptom | Possible cause | Recommended action |
|----------|----------------|--------------------|
| Large replicate variation | Air bubbles or insufficient mixing | Mix gently and remove visible bubbles before measurement. |
| Negative or below-zero calculated result | Sample signal below the stored blank or blank mismatch | Measure a fresh reagent blank and verify the calibration. Do not report a negative dsDNA concentration; apply the LOD/LOQ reporting rules from Chapter 9. |
| Unexpectedly low concentration | Pipetting error or degraded reagent | Verify pipetting accuracy and reagent quality. |
| Unexpectedly high concentration | Sample contamination | Prepare a fresh aliquot and repeat the measurement. |
| Measurement exceeds calibration range | Sample concentration above the validated range | Dilute the sample and repeat the analysis. |

## Calibration Suite

| Symptom | Possible cause | Recommended action |
|----------|----------------|--------------------|
| CSV file cannot be imported | Incorrect or unsupported CSV structure | Check the delimiter, column headers, decimal format, and required calibration-data columns. |
| Calibration model unavailable | Insufficient calibration points | Acquire additional standards covering the required concentration range. |
| Exported JSON rejected | Calibration incomplete | Complete the calibration workflow before exporting. |

## Preventive Maintenance

To ensure reproducible analytical performance:

- keep the optical compartment clean and free of dust;
- inspect optical filters regularly for contamination or damage;
- use clean PCR tubes for every measurement;
- ensure that the selected power source is sufficiently charged before extended measurement sessions;
- periodically verify the instrument using a quality-control sample.

## Quick Troubleshooting Guide

| Problem | Section |
|----------|---------|
| Device does not start | Hardware |
| LED or sensor not working | Hardware |
| Calibration cannot be loaded | Firmware and Software |
| Calibration rejected | Calibration |
| Unexpected measurement results | Measurement |
| CSV or JSON problems | Calibration Suite |

---

⬅️ Previous Chapter: [Validation and Analytical Performance](10_validation_and_analytical_performance.md)

📖 [Documentation Summary](SUMMARY.md)

➡️ Next Chapter: [Workshop Review, Quality Check and Further Applications](12_workshop_exercises_and_checklists.md)