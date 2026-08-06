# Troubleshooting

This chapter summarizes the most common operational problems that may occur during assembly, firmware installation, calibration, and routine measurements. It is intended as a practical troubleshooting guide for workshop participants and laboratory users. More detailed background information is provided in the previous chapters.

---

## Hardware

| Symptom | Possible cause | Recommended action |
|----------|----------------|--------------------|
| Display remains dark | Battery discharged | Recharge the PyBadge or connect USB power. |
| Device does not start | CircuitPython not installed correctly | Repeat the firmware installation (Chapter 7). |
| LED does not illuminate | Loose cable or incorrect connector | Verify all wiring and connector orientation. |
| Sensor not detected | Qwiic/STEMMA cable disconnected | Check the cable and I²C connections. |
| Very low fluorescence signal | Optical filters installed incorrectly | Verify the orientation and seating of both optical filters. |
| Signal permanently saturated | Sample concentration too high | Dilute the sample before measurement. |

---

## Firmware and Software

| Symptom | Possible cause | Recommended action |
|----------|----------------|--------------------|
| Calibration cannot be loaded | Missing or incompatible JSON file | Export the calibration again using the Calibration Suite. |
| Calibration import fails | Invalid JSON format | Validate the calibration file before copying it to the device. |
| Device reports "uncalibrated" | No calibration selected | Load a valid calibration before measuring samples. |
| Device freezes during startup | Incomplete firmware installation | Reinstall the firmware according to Chapter 5. |

---

## Calibration

| Symptom | Possible cause | Recommended action |
|----------|----------------|--------------------|
| Blank values unstable | Ambient light or contaminated PCR tube | Repeat the blank measurement using a clean tube under stable conditions. |
| Calibration rejected | Standards prepared incorrectly | Prepare fresh standards and repeat the calibration. |
| Unknown outside calibration range | Sample concentration exceeds the validated range | Dilute the sample and repeat the measurement. |
| High calibration uncertainty | Pipetting errors or degraded standards | Prepare fresh standards and recalibrate. |

---

## Measurement

| Symptom | Possible cause | Recommended action |
|----------|----------------|--------------------|
| Large replicate variation | Air bubbles or insufficient mixing | Mix gently and remove visible bubbles before measurement. |
| Negative concentration | Blank mismatch | Repeat the blank measurement and verify the calibration. |
| Unexpectedly low concentration | Pipetting error or degraded reagent | Verify pipetting accuracy and reagent quality. |
| Unexpectedly high concentration | Sample contamination | Prepare a fresh aliquot and repeat the measurement. |
| Measurement exceeds calibration range | Sample concentration above the validated range | Dilute the sample and repeat the analysis. |

---

## Calibration Suite

| Symptom | Possible cause | Recommended action |
|----------|----------------|--------------------|
| CSV file cannot be imported | Incorrect file format | Verify that the CSV file matches the required template. |
| Calibration model unavailable | Insufficient calibration points | Acquire additional standards covering the required concentration range. |
| Exported JSON rejected | Calibration incomplete | Complete the calibration workflow before exporting. |

---

## Preventive Maintenance

To ensure reproducible analytical performance:

- keep the optical compartment clean and free of dust;
- inspect optical filters regularly for contamination or damage;
- use clean PCR tubes for every measurement;
- recharge the battery before extended measurement sessions; and
- periodically verify the instrument using a quality-control sample.

---

## Quick Troubleshooting Guide

| Problem | Section |
|----------|---------|
| Device does not start | Hardware |
| LED or sensor not working | Hardware |
| Calibration cannot be loaded | Firmware and Software |
| Calibration rejected | Calibration |
| Unexpected measurement results | Measurement |
| CSV or JSON problems | Calibration Suite |
