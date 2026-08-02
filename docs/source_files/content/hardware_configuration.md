# Defined Hardware Configuration

This file is reusable source content for the theory chapter, BOM notes, and assembly documentation.

| Component | Defined project configuration | Function |
|---|---|---|
| Excitation LED | 5 mm radial 485 nm “Ice Blue/Cyan”; 30°; 12,000 mcd; 3.2 V; article 1030055 | Excites the QuantiFluor® ONE dye–dsDNA complex |
| LED board | ioRodeo `i_control_led`, I²C, SMD0603 production `ver_0p1_rev_2`, 16 mA, STEMMA QT | Controls LED operation |
| Excitation filter | Neemoo Ex470BP-40, installed | Defines the excitation band |
| Sample vessel | Promega thin-walled 0.5 mL PCR tube, Cat. No. E4941 | Holds blank, standards, and samples |
| Optical geometry | One TSL2591 sensor at 90° to the excitation axis | Reduces direct excitation light at the detector |
| Emission filter | Neemoo Em532BP-40, installed | Passes fluorescence and suppresses excitation light |
| Sensor | Adafruit TSL2591, Product ID 1980, PCB revision 2023-10-24, STEMMA QT, I²C `0x29` | Measures the fluorescence signal |
| Multiplexer | Adafruit PCA9546 four-channel STEMMA QT/Qwiic multiplexer, project inventory Product ID 5664, I²C `0x70` | Selects the LED and sensor I²C channels |
| Controller | Adafruit PyBadge, Product ID 4200 | Runs CircuitPython firmware and user interface |
| Adapter | SparkFun Qwiic–Grove cable, 100 mm, PRT-15109 | Connects PyBadge I²C/Grove to Qwiic/STEMMA QT |
| Internal cables | STEMMA QT/Qwiic JST SH four-pin cables | Connects multiplexer, LED board, and sensor |

## Electrical connection overview

```text
Adafruit PyBadge 4200
        │ I²C/Grove
SparkFun PRT-15109 adapter
        │ Qwiic/STEMMA QT
Adafruit PCA9546 multiplexer, 0x70
        ├── configured channel → ioRodeo 16 mA LED board
        └── configured channel → Adafruit TSL2591, 0x29
```

## Calibration-critical configuration

The following are part of the calibration: LED and current, excitation and emission filters, sample vessel and insertion geometry, sensor position, TSL2591 gain and integration time, reagent and lot, assay volumes, and blank preparation.
