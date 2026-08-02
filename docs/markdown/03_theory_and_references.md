# DIY-QuantiFluorONE-dsDNA-Fluorometer – Theory and References

> **Document status:** Draft  
> **Validation status:** Not yet validated  
> **Date:** 2026-08-02

## Purpose and practical scope

This chapter provides the minimum theory needed to understand, calibrate, and use the DIY-QuantiFluorONE-dsDNA-Fluorometer in a workshop. It is not intended to be a complete textbook on fluorescence spectroscopy or analytical-method validation.

The instrument uses off-the-shelf optical and electronic components, one fluorescence sensor, a fixed 90° optical geometry, and the Promega QuantiFluor® ONE dsDNA assay. Quantitative results are obtained only after blank measurement and calibration. The current repository status and the analytical validation status must always be reported separately.

> **Workshop objective:** Prepare a reagent blank, standards, and unknown samples; measure the blank-corrected fluorescence response; apply a two-point or multipoint calibration; and interpret the result within the calibrated working range.

## Fluorescence in brief

A fluorophore absorbs excitation light and reaches an electronically excited state. Part of the absorbed energy is then emitted as fluorescence at a longer wavelength. The separation between the excitation and emission maxima is the **Stokes shift**.

For the QuantiFluor® ONE dsDNA dye, Promega specifies an excitation maximum of 504 nm and an emission maximum of 531 nm. The nominal Stokes shift is therefore about 27 nm [1].

Within a suitable working range, the fluorescence response increases with the amount of dye-bound dsDNA. The measured signal is also influenced by excitation intensity, filter transmission, sample-vessel geometry, dye binding, sensor settings, temperature, and sample matrix. At high concentrations, detector saturation, inner-filter effects, or dye-response nonlinearity may occur [2,3].

Important practical effects are background, quenching, photobleaching, and chemical or optical interference. They are controlled primarily by using a matching reagent blank, identical tubes and geometry, consistent incubation and reading times, and calibration standards prepared in a suitable matrix.

## Optical architecture

```text
485 nm nominal radial LED
        ↓
Neemoo Ex470BP-40 excitation filter
        ↓
Promega E4941 thin-walled 0.5 mL PCR tube
        ↓
QuantiFluor® ONE dye–dsDNA fluorescence
        ↓  at 90° to the excitation axis
Neemoo Em532BP-40 emission filter
        ↓
one Adafruit TSL2591 fluorescence sensor
```

The TSL2591 sensor axis is positioned **at 90°** to the excitation axis. This geometry reduces direct illumination of the sensor by the excitation beam. Geometry, tube position, filters, LED current, gain, and integration time are part of the calibration.

### Installed components

| Component | Installed configuration | Practical role |
|---|---|---|
| Excitation LED | 5 mm radial 485 nm “Ice Blue/Cyan” LED; 30°; 12,000 mcd; 3.2 V; article 1030055 | Excites the dye–dsDNA complex |
| LED control board | ioRodeo `i_control_led` I²C board, SMD0603 production version, 16 mA | Provides defined LED operation |
| Excitation filter | Neemoo Ex470BP-40 | Selects the useful excitation band |
| Sample vessel | Promega thin-walled 0.5 mL PCR tube, Cat. No. E4941 | Defines the assay and geometry |
| Emission filter | Neemoo Em532BP-40 | Passes green fluorescence and suppresses excitation light |
| Sensor | Adafruit TSL2591, Product ID 1980, I²C `0x29` | Measures filtered fluorescence |
| Multiplexer | Adafruit PCA9546 four-channel STEMMA QT/Qwiic multiplexer, project inventory Product ID 5664, `0x70` | Selects I²C channels |
| Controller | Adafruit PyBadge, Product ID 4200 | Runs firmware and stores results |
| Cabling | STEMMA QT/Qwiic cables and SparkFun PRT-15109 adapter | Connects the I²C system |

The design builds on the open ioRodeo Open Colorimeter Plus ecosystem [4,5]. Component identities and connections are documented by Adafruit and SparkFun [12–15].

### Filter verification

The supplier provides the nominal filter designation and percentage-transmittance information [16]. The installed filters were additionally checked with the project’s DIY spectrometer based on PySpectrometer2 [6]. The curves were normalized to their individual maxima and used to verify passband position and shape:

- Ex470BP-40: approximate half-maximum interval 450–490 nm;
- Em532BP-40: approximate half-maximum interval 518–555 nm.

![Spectral verification of the installed Neemoo Ex470BP-40 excitation filter.](../figures/source/qfo_ex470bp40_spectral_verification.jpeg)

![Spectral verification of the installed Neemoo Em532BP-40 emission filter.](../figures/source/qfo_em532bp40_spectral_verification.jpeg)

## Signal formation and blank correction

```text
VIS_i = max(FULL_i − IR_i, 0)
VIS = mean of three technical sensor readings
RFU = VIS_sample − VIS_blank
```

RFU means **relative fluorescence unit**. It is instrument-dependent. Signed RFU values are retained in the raw data. A negative RFU indicates a response below the stored blank, not a negative physical DNA concentration.

Measure a new blank when the reagent lot, tube type, optical arrangement, sensor settings, temperature conditions, or measurement session changes.

## dsDNA quantification with QuantiFluor® ONE

Promega specifies 504 nm excitation, 531 nm emission, and a nominal range of 0.2–400 ng dsDNA input. The kit includes QuantiFluor® ONE Lambda DNA at 400 µg/mL [1].

The project uses:

```text
1 µL sample or standard + 200 µL reagent = 201 µL physical total volume
```

Use thin-walled 0.5 mL PCR tubes, mix without bubbles, incubate for five minutes at room temperature protected from light, and pipette the small sample volume carefully [1]. Record the λ-DNA supplier, product, lot, stock concentration, dilution medium, preparation date, and storage conditions.

## Calibration

The linear model is:

```text
y = a + b x
x̂ = (y − a) / b
```

where `y` is RFU and `x` is the selected concentration or DNA-mass basis.

### Two-point calibration

```text
b = RFU_standard / x_standard
x_sample = RFU_sample / b
```

Two-point calibration is fast and practical, but it does not test linearity across a range.

### Multipoint calibration

Calibration Suite 7.2 Stable uses several concentration levels and replicates. It can calculate OLS and compare weighted models (`1/c`, `1/c²`, `1/s²`), and it reports residuals, confidence and prediction bands, recovery, and model statistics. The current PyBadge firmware imports accepted OLS calibration data.

DIN 38402-51:2017-05 is cited as a reference for linear calibration concepts [7].

> **Practical rule:** Do not report a sample quantitatively outside the calibrated range. Dilute or re-prepare it and measure again.

## LOD and LOQ

LOD and LOQ depend on the procedure, calibration, blank variability, and dataset.

### Two-point firmware estimate

Ten independently prepared reagent blanks are each measured as one three-reading cycle:

```text
LOD estimate = 3 × s_blank / slope
LOQ estimate = 10 × s_blank / slope
```

These are transparent blank-based estimates, not a complete formal implementation of DIN 32645.

### Multipoint calculation

Calibration Suite 7.2 Stable implements the indirect calibration-curve calculation documented in the software as the DIN 32645 method summarized in CLB1. It uses the residual standard deviation, slope, Student-t factors, calibration design, significance level, quantification factor `k`, and number of future determinations; LOQ is solved iteratively.

DIN 32645:2008-11 is the relevant standards reference [8]. A formal conformity claim requires a documented comparison with the licensed standard.

## Reference projects and commercial comparison

| System | Role | Main distinction |
|---|---|---|
| ioRodeo Open Colorimeter Plus | Open hardware and CircuitPython reference platform | General technical base |
| DIYNAFLUOR | Open-source reference for a low-cost 90° TSL2591 fluorometer | Developed mainly for Qubit assays and two-point calibration |
| DIY-QuantiFluorONE | Workshop instrument described here | QuantiFluor® ONE, Ex470BP-40, Em532BP-40, one TSL2591 at 90°, 2PT and imported MP calibration |
| Promega Quantus™ | Commercial reference instrument | 470 nm blue excitation peak, 510–580 nm blue emission band, manufacturer workflow |

DIYNAFLUOR demonstrates a practical fluorometer assembled from off-the-shelf and 3D-printed parts [9,10]. Quantus™ is a useful commercial reference, but bias or agreement must be established using the same standards on both instruments [11].

## Practical validity conditions

Recalibrate or verify after changing the LED, current, filters, tube, holder, optical alignment, TSL2591 settings, sensor board, multiplexer channel, reagent lot, assay volumes, concentration basis, or blank preparation.

During workshop measurements:

1. Use the same tube type for blank, standards, and unknowns.
2. Keep orientation and insertion depth consistent.
3. Avoid bubbles, fingerprints, scratches, and droplets above the liquid.
4. Mix and incubate consistently and protect tubes from light.
5. Measure a reagent blank before samples.
6. Use standards that bracket the samples.
7. Repeat or dilute results outside the calibrated range.
8. Retain FULL, IR, VIS, blank, RFU, calibration ID, and result data.

The instrument is intended for research, teaching, and workshop use, not clinical diagnosis. The supplier’s nominal assay range is not automatically the validated range of the assembled device.

## Workshop take-away

```text
Prepare blank and standards
→ incubate consistently
→ measure one TSL2591 at 90°
→ calculate VIS and blank-corrected RFU
→ apply calibration
→ check range and LOD/LOQ
→ save raw and calculated data
```

## References

1. Promega Corporation. *QuantiFluor® ONE dsDNA System Technical Manual*. TM405, revised 10/22.
2. Lakowicz JR. *Principles of Fluorescence Spectroscopy*. 3rd ed. Springer; 2006.
3. Valeur B, Berberan-Santos MN. *Molecular Fluorescence: Principles and Applications*. 2nd ed. Wiley-VCH; 2012.
4. ioRodeo. *Open Colorimeter Plus firmware*. GitHub repository.
5. ioRodeo. *i_control_led I²C radial LED board*. GitHub repository.
6. Wright L. *PySpectrometer2*. GitHub repository.
7. DIN 38402-51:2017-05. *Calibration of analytical methods—Linear calibration (A 51)*.
8. DIN 32645:2008-11. *Decision limit, detection limit and determination limit under repeatability conditions*.
9. Anderson W, et al. *DIYNAFLUOR: An Affordable DIY Plug-and-Play Nucleic Acid Fluorometer for eDNA Quantification in Resource Limited Settings*. bioRxiv preprint; 2024. doi:10.1101/2024.12.16.626200.
10. Trau Lab. *DIYNAFLUOR*. GitHub repository.
11. Promega Corporation. *Quantus™ Fluorometer Operating Manual*. TM396, revised 11/24.
12. Adafruit Industries. *TSL2591 High Dynamic Range Digital Light Sensor, Product ID 1980*.
13. Adafruit Industries. *PCA9546 4-Channel I²C Multiplexer*.
14. Adafruit Industries. *Adafruit PyBadge, Product ID 4200*.
15. SparkFun Electronics. *Qwiic Cable—Grove Adapter, 100 mm, PRT-15109*.
16. Neemoo. *Optical Band-Pass Filters, AliExpress Item 1005010613836251*. Supplier listing.
