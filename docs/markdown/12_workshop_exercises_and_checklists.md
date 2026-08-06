# Workshop Review, Quality Check and Further Applications

This chapter concludes the workshop with a brief review of the practical exercises, a final functional quality check, and an outlook on additional fluorescence-based applications that can be implemented using the modular DIY-QuantiFluorONE-dsDNA-Fluorometer platform.

---

## Functional Quality Check

Before completing the workshop, verify that the instrument performs the following tasks successfully.

| Step | Expected result |
|------|-----------------|
| Power on the instrument | Device starts normally |
| Perform a blank measurement | Stable blank signal |
| Measure a quality-control standard | Result within the expected acceptance range |
| Repeat the measurement | Comparable concentration and repeatability |
| Save the measurement | CSV file created successfully |
| Load a stored calibration | Calibration accepted without errors |

Successful completion of these checks confirms that the instrument is ready for routine measurements.

---

## Workshop Review

The following questions may be used for self-assessment or group discussion.

### Instrument

- Why is fluorescence detected at 90° to the excitation beam?
- Why are excitation and emission filters required?
- Why is a blank measurement performed before sample analysis?

### Calibration

- When should a sample be diluted before measurement?
- What indicates that a calibration should be repeated?
- Why should quality-control samples be measured regularly?

### Practical Operation

- Which file stores the calibration?
- Which file stores the measurement results?
- Which file is transferred from the Calibration Suite to the fluorometer?
- Why should calibration and validation data always be archived?

---

## Further Applications

The DIY-QuantiFluorONE-dsDNA-Fluorometer is a modular fluorescence platform. By exchanging the excitation LED, optical filters and calibration, the same hardware can be adapted to many fluorescence-based analytical methods.

| Example application | Excitation LED | Emission wavelength | Typical application |
|---------------------|---------------:|--------------------:|--------------------|
| dsDNA (QuantiFluor® ONE) | 485 nm | 530 nm | DNA quantification |
| Chlorophyll-a | 450 nm | 680 nm | Phytoplankton and algal biomass |
| CDOM | 350 nm | 425 nm | Colored dissolved organic matter |
| Ammonium (OPA derivatisation) | 350 nm | 425 nm | Nutrient analysis |

These examples illustrate the flexibility of the optical platform and do not represent a complete list of possible fluorescence assays.

Future applications may require different LEDs, optical filters, detector settings and calibration procedures depending on the fluorophore being analysed.

---

## Workshop Completed

Congratulations!

You have successfully completed the DIY-QuantiFluorONE-dsDNA-Fluorometer workshop.

Participants should now be able to:

- assemble the instrument;
- install the firmware and software;
- perform blank, calibration and routine measurements;
- evaluate measurement quality and analytical performance; and
- understand how the same modular platform can be adapted to many other fluorescence-based analytical methods.

We encourage participants to further develop the platform, evaluate additional fluorescence assays and contribute improvements to the open-source project.

---

⬅️ Previous Chapter: [Troubleshooting](11_troubleshooting.md)

📖 [Documentation Summary](SUMMARY.md)

➡️ Next Chapter: [References and Acknowledgements](13_references.md)