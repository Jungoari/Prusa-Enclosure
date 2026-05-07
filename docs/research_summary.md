# Research Summary

## Research question

Can a 3D printer detect nozzle clogging earlier by looking at air-quality and process signals instead of relying only on camera images?

## System

The research uses a Prusa MK3S platform inside a custom enclosure. The monitoring system combines:

- PMS7003 particulate matter sensing,
- SGP30 TVOC/eCO2 sensing,
- DHT22 temperature and humidity sensing,
- printer metadata,
- a closed-loop chamber and filter structure,
- inlet/outlet sensor comparison.

Sensor values and printer metadata are aligned on a common timestamp at 1 Hz.

## Feature design

The paper uses differential features between the inlet and outlet sensor positions:

- `TVOC_diff = TVOC_in - TVOC_out`
- `PM2_5_diff = PM2_5_in - PM2_5_out`
- `TVOC_eff = (TVOC_in - TVOC_out) / TVOC_in`
- `PM2_5_eff = (PM2_5_in - PM2_5_out) / PM2_5_in`

TVOC is also interpreted with humidity compensation using DHT22 measurements because SGP30 readings are affected by temperature and humidity.

## Labeling and model

Nozzle clogging is defined using a persistence rule over `TVOC_diff`:

- compute a 60-second moving average,
- treat the state as abnormal when the smoothed value remains above the threshold persistently,
- use 60-second multivariate time-series windows for data-driven classification.

The paper uses a time-preserving 80:20 split and evaluates Accuracy, Precision, Recall, F1-score, and ROC AUC.

## Results

| Metric | Value |
|---|---:|
| Accuracy | 0.951085 |
| Precision | 0.946218 |
| Recall | 0.999913 |
| F1-score | 0.972325 |
| ROC AUC | 0.975934 |
| Early warning lead time | 472 seconds |

The strongest result is the very high recall for the clogging class. The system reached the warning threshold 472 seconds before the rule-defined clogging label transition.

## Interpretation

This is promising as an early-warning system, but not yet a final general-purpose clogging detector. The paper notes that some normal samples were classified as clogging. Therefore, the current result should be described as a conservative, high-sensitivity warning model that still needs:

- physical ground-truth labeling,
- false-alarm reduction,
- validation under more materials and print conditions,
- edge-device latency and resource measurements.
