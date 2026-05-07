#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python analysis/plot_sensor_comparison.py \
  --sensor1 data/sample/sensor1_sample.csv \
  --sensor2 data/sample/sensor2_sample.csv \
  --out docs/images
