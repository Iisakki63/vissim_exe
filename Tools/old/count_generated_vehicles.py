# -*- coding: utf-8 -*-
"""
Count generated vehicles from a Vissim .fhz file.

Output groups:
  - All vehicles
  - Cars (VehType 100)
  - Bikes (VehType 600 by default; use --bike-type 610 if your model uses 610)
  - Links (vehicle counts per Link)

Usage:
  python count_generated_vehicles.py input.fhz output.txt
  python count_generated_vehicles.py input.fhz output.txt --bike-type 610
"""

import argparse
from pathlib import Path
import pandas as pd


def read_vissim_fhz(filepath: str) -> pd.DataFrame:
    """Read the vehicle-entered table from a Vissim .fhz file."""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
        lines = file.read().splitlines()

    header_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith("Time;"):
            header_index = i
            break

    if header_index is None:
        raise ValueError("Could not find the .fhz table header starting with 'Time;'.")

    columns = [col.strip().replace(".", "") for col in lines[header_index].split(";") if col.strip()]

    rows = []
    for line in lines[header_index + 1:]:
        if not line.strip() or ";" not in line:
            continue
        values = [val.strip() for val in line.split(";") if val.strip()]
        if len(values) == len(columns):
            rows.append(values)

    if not rows:
        raise ValueError("No vehicle rows found in the .fhz file.")

    df = pd.DataFrame(rows, columns=columns)
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    required_columns = {"Link", "VehNo", "VehType"}
    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Missing required column(s): {', '.join(sorted(missing))}")

    return df


def make_report(df: pd.DataFrame, inpfilepath: str, bike_type: int) -> str:
    all_count = len(df)
    car_count = int((df["VehType"] == 100).sum())
    bike_count = int((df["VehType"] == bike_type).sum())

    link_counts = (
        df.groupby("Link")
        .size()
        .reset_index(name="Count")
        .sort_values("Link")
    )

    veh_type_counts = (
        df.groupby("VehType")
        .size()
        .reset_index(name="Count")
        .sort_values("VehType")
    )

    lines = []
    lines.append("Generated vehicle count from Vissim .fhz")
    lines.append(f"Input file: {inpfilepath}")
    lines.append("")
    lines.append("Summary")
    lines.append(f"All: {all_count}")
    lines.append("Cars (type 100): {}".format(car_count))
    lines.append("Bikes (type {}): {}".format(bike_type, bike_count))
    lines.append("")
    lines.append("Vehicle types found")
    lines.append(veh_type_counts.to_string(index=False))
    lines.append("")
    lines.append("Links")
    lines.append(link_counts.to_string(index=False))

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Count generated vehicles from a Vissim .fhz file.")
    parser.add_argument("input_fhz", help="Input .fhz file")
    parser.add_argument("output_txt", help="Output text file")
    parser.add_argument(
        "--bike-type",
        type=int,
        default=600,
        help="VehType value used for bikes. Default: 600. Some Vissim files use 610.",
    )
    args = parser.parse_args()

    df = read_vissim_fhz(args.input_fhz)
    report = make_report(df, args.input_fhz, args.bike_type)

    print(report)
    Path(args.output_txt).write_text(report + "\n", encoding="utf-8")
    print(f"\nWrote: {args.output_txt}")


if __name__ == "__main__":
    main()
