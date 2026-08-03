# Upstream source record — ioRodeo radial 16 mA LED board

- Upstream project: `iorodeo/i_control_led`
- Repository: https://github.com/iorodeo/i_control_led
- Hardware path: `fixed/5V_regulator/radial_16mA`
- Installed revision: `ver_0p1_rev_3`
- Production path: `production/ver_0p1_rev_3`
- Retrieval date for KiCad sources and licence: 2026-08-03
- Licence: CC BY 4.0

The board provides a fixed LED current of approximately 16 mA. Its schematic
notes specify `I(LED) = Vset / R1`, with `R1 = 10 ohm` and `Vset = 0.16 V`.
The board has no I²C device address; the SDA and SCL nets are routed between the
two four-pin connectors.

The wavelength-specific 5 mm radial LED is installed separately and must be
oriented according to PCB polarity markings before power is applied.
