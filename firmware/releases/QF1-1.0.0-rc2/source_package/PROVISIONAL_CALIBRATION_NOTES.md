# Provisional Calibration Notes

## Intended use

The included `quantifluorone_multipoint.json` is supplied only to test the complete v1.0 firmware workflow:

- JSON import;
- persistent calibration storage;
- blank correction;
- concentration prediction;
- prediction intervals;
- LOD/LOQ display;
- range warnings;
- CSV export;
- restart persistence.

It is not an independent analytical validation.

## Data treatment

- Dilution factor: 201.
- Zero level: mean of ten v0.60 blank measurement cycles.
- Positive levels: mean of the first and second v0.5.2 measurement cycles.
- Assigned concentrations: 5.5, 10, 75, 250, 375 and 670 ng/µL.
- `Sample_100` was treated as a zero-like diagnostic sample and excluded from the regression.
- All ten individual blank values remain in the JSON and source-data CSV for transparency.

The ten blank observations are used to calculate the blank SD and LOD/LOQ. The regression uses one mean value for the zero concentration level so that the blank level is not weighted ten times more heavily than each positive level.

## Photobleaching and time drift

Five of six positive levels produced a lower RFU during the second measurement. The included regression uses the two-cycle mean only because this is a firmware test. A validated calibration should use a predefined exposure protocol with fresh standards and should avoid uncontrolled repeated illumination.

## Mechanical and volumetric limitations

The dataset was affected by:

- an excitation LED that was not yet mechanically rigid;
- an unreliable pipette and pipette tips;
- aged standards;
- possible tube-orientation effects;
- possible fluorescence bleaching.

## Replacement criteria

Replace this JSON before reporting validated analytical results. The replacement should use fresh standards, reliable volumetric equipment, a fixed LED, independent measurements with the commercial QuantiFluor instrument, and an accepted Calibration Suite regression.
