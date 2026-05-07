"""Plot two Prusa Enclosure sensor logs.

Usage:
    python analysis/plot_sensor_comparison.py \
      --sensor1 data/sample/sensor1_sample.csv \
      --sensor2 data/sample/sensor2_sample.csv \
      --out docs/images
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

COLUMNS = ["TVOC_ppb", "eCO2_ppm", "PM1_0", "PM2_5", "PM10", "temp_C", "hum_%"]

def load(path: Path, max_points: int = 6000) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["timestamp"], on_bad_lines="skip")
    for col in COLUMNS:
        if col in df:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df.loc[df[col] > 10000, col] = pd.NA
    if len(df) > max_points:
        step = max(1, len(df) // max_points)
        df = df.iloc[::step].copy()
    return df

def plot_pair(df1, df2, col, ylabel, title, out):
    plt.figure(figsize=(12, 4.8))
    plt.plot(df1["timestamp"], df1[col], label="Sensor 1", linewidth=1.2)
    plt.plot(df2["timestamp"], df2[col], label="Sensor 2", linewidth=1.2)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel(ylabel)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out, dpi=160)
    plt.close()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sensor1", type=Path, required=True)
    ap.add_argument("--sensor2", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    df1, df2 = load(args.sensor1), load(args.sensor2)
    plot_pair(df1, df2, "TVOC_ppb", "TVOC (ppb)", "TVOC comparison between two enclosure sensor modules", args.out / "20_tvoc_comparison.png")
    plot_pair(df1, df2, "PM2_5", "PM2.5", "PM2.5 comparison between upstream/downstream sensors", args.out / "21_pm25_filter_comparison.png")

if __name__ == "__main__":
    main()
