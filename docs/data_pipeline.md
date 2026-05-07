# Data Pipeline

The data pipeline is designed around synchronized 1 Hz records.

## Sensor packet

Each sensor log row follows this shape:

```text
timestamp, sensor_id, temp_C, hum_%, TVOC_ppb, eCO2_ppm, PM1_0, PM2_5, PM10
```

## Target synchronized record

Future records should combine sensor values with printer metadata from Moonraker:

```json
{
  "timestamp": "2026-05-07T12:00:00+09:00",
  "print_id": "pla_test_001",
  "printer_state": "printing",
  "layer": 37,
  "progress_percent": 42.1,
  "nozzle_temp_c": 215.0,
  "bed_temp_c": 60.0,
  "fan_percent": 80,
  "pm2_5_upstream": 5,
  "pm2_5_downstream": 2,
  "tvoc_upstream_ppb": 180,
  "tvoc_downstream_ppb": 95,
  "temperature_c": 32.0,
  "humidity_percent": 41.5,
  "failure_probability": 0.03,
  "label": "normal"
}
```

## Feature ideas

- rolling mean / median,
- temporal gradient,
- upstream vs downstream difference,
- humidity-compensated TVOC,
- PM2.5 and PM10 persistence,
- z-score relative to recent baseline,
- printer progress and layer-aware features.

## Plotting

Generate example plots from two logs:

```bash
python analysis/plot_sensor_comparison.py \
  --sensor1 data/sample/sensor1_sample.csv \
  --sensor2 data/sample/sensor2_sample.csv \
  --out docs/images
```

For full logs, place them outside the Git repo or use Git LFS / external storage.
