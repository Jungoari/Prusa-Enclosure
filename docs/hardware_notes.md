# Hardware Notes

## Printer

- Base printer: Prusa MK3S
- Firmware direction: Klipper
- Host: Raspberry Pi
- Replacement board: SKR Mini E3 V3.0
- Stepper drivers: TMC2209
- Z probe direction: SuperPINDA-based probing

## Sensors

| Module | Measurement | Notes |
|---|---|---|
| PMS7003 | PM1.0 / PM2.5 / PM10 | Particle measurement |
| SGP30 | TVOC / eCO2 | VOC-related monitoring |
| DHT22 | Temperature / humidity | Chamber environmental context |

## Enclosure

- Lower room: Printing Room
- Upper room: Filament Room
- Filtration: HEPA + activated carbon
- Concept: internal closed-loop air recirculation

## Open items before final release

- Confirm final Klipper pin mapping.
- Commit tested `printer.cfg` and macros.
- Confirm final sensor MCU board and pinout.
- Clean up sensor hub firmware.
- Confirm whether LCD dashboard is a persistent service or prototype.
- Add safety notes for heaters, fans, wiring, and enclosure operation.
