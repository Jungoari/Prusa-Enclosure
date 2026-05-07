# Build Log

This is a condensed build narrative for **Prusa Enclosure V1.0**.

## 1. Starting point

The project started from a used Prusa MK3S. The first goal was remote monitoring and easier print supervision, so a Raspberry Pi and camera-based setup were used early on.

The project later grew into a full enclosure and sensing platform because printing materials beyond PLA requires better environmental control, and because filament humidity and chamber stability strongly affect print quality.

## 2. Enclosure design

The enclosure was planned as a two-level structure:

- lower **Printing Room** for the Prusa MK3S,
- upper **Filament Room** for storage and future humidity control.

A domestic aluminum profile was selected instead of the typical European 2020 extrusion profile. The 3030 profile slot dimensions were close enough to reuse many existing design ideas while keeping cost manageable.

Custom brackets were modeled and printed where metal brackets were not necessary. Stronger print settings were used for structural parts: more walls, higher infill, slower speed, and careful orientation.

## 3. Klipper conversion

The original Prusa electronics were removed and replaced with an SKR Mini E3 V3.0 board. This required re-crimping and labeling many wires because connector types and pin ordering did not match directly.

Important work included:

- rewiring motor phases correctly,
- configuring Klipper through Raspberry Pi,
- installing Fluidd / web dashboard tooling,
- tuning motor direction and movement,
- testing sensorless homing,
- preserving the Z-probe concept with SuperPINDA.

A major lesson was that a motor not moving correctly is not always a motor problem. In this build, wiring order and coil pairing were critical.

## 4. Fans, heaters, and calibration

Several issues appeared during bring-up:

- fan voltage mismatch caused a fan failure,
- slicer output had to be changed from Marlin-style assumptions to Klipper-compatible G-code,
- heater performance required replacement and PID tuning,
- Z offset and first-layer calibration had to be repeated many times,
- nozzle leaks and clogs required mechanical rebuilds.

The calibration process included:

- PID tuning,
- extrusion / rotation distance calibration,
- Z-offset tuning,
- bed mesh checks,
- flow-rate calibration,
- pressure advance experiments.

## 5. Filtration and sensing

The enclosure was extended with an internal closed-loop filtration concept using HEPA and activated carbon. Sensor modules were placed to compare air before and after the filter path.

The sensing stack focuses on:

- particulate matter: PM1.0 / PM2.5 / PM10,
- VOC-related values: TVOC / eCO2,
- environmental variables: temperature and humidity.

The long-term value of these sensors is not just display. The plan is to connect environmental changes to printer state and detect abnormal printing behavior.

## 6. Data logging

Two large logs were collected from the sensor modules. They contain timestamped measurements for temperature, humidity, TVOC, eCO2, and PM values.

The full logs are not included in this repository because they are large. Instead, small samples and plotting code are provided.

## 7. Current direction

The project is now moving from “hardware build” to “experimental platform.” The most important next steps are:

1. clean up final firmware and Klipper configuration,
2. synchronize sensor logs with Moonraker printer metadata,
3. build a robust feature extraction pipeline,
4. evaluate filter performance,
5. prototype nozzle clogging / extrusion failure detection.
