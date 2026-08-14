---
document-status: "Current"
validation-status: "Validated configuration"
date:  "2026-08-14"
---

This chapter concludes the workshop with a brief review of the practical exercises, a final functional quality check, and an outlook on possible future applications of the underlying modular fluorescence platform.

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

Successful completion of these checks confirms correct basic instrument operation. Quantitative results should only be accepted when the calibration, blank, quality-control, range, and reporting criteria described in Chapter 9 are also satisfied.

## Workshop Review

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

## Further Applications

The DIY-QuantiFluorONE-dsDNA-Fluorometer described in this booklet is configured and evaluated specifically for the Promega QuantiFluor® ONE dsDNA assay.

The underlying instrument concept is modular. By selecting an appropriate excitation source, optical filters, detector settings, sample geometry, and calibration procedure, the same general design approach can provide a basis for other fluorescence-based analytical applications.

The examples below summarize possible starting points for further instrument development. The excitation and emission wavelengths are indicative optical design parameters for the respective fluorescence methods; they do not imply that these applications have been validated with the present DIY-QuantiFluorONE configuration.

| Example application | Excitation LED | Emission wavelength | Typical application |
|---------------------|---------------:|--------------------:|--------------------|
| dsDNA (QuantiFluor® ONE) | 485 nm | 530 nm | DNA quantification |
| Chlorophyll-a | 450 nm | 680 nm | Phytoplankton and algal biomass |
| CDOM | 350 nm | 425 nm | Colored dissolved organic matter |
| Ammonium (OPA derivatisation) | 350 nm | 425 nm | Nutrient analysis |
| PAK (Naphtalene and derivates) | 275 nm | UVA with AS7331 | SPE from seawater |

These examples illustrate how the modular optical concept may be extended beyond dsDNA quantification. They do not constitute validated instrument configurations or complete analytical methods.

Future applications may require different LEDs, excitation and emission filters, detector settings, sample holders, firmware parameters, and calibration procedures. Each modified configuration should therefore be characterized and validated for its intended analytical application before quantitative results are reported.

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