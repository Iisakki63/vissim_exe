# -*- coding: utf-8 -*-
"""
Count generated vehicles from a Vissim .fhz file.

Usage:
    python count_generated_vehicles.py input.fhz links.txt output.txt

The program ignores the text header at the beginning of the .fhz file.
It starts reading data only after the semicolon-separated column header:
    Time; Link; Lane; VehNo; VehType; Line; DesSpeed;

Vehicle classes:
    All vehicles  = all rows in the .fhz table
    Cars          = VehType 100 or 200
    Bikes         = VehType 610
"""

import sys
import re
from collections import Counter


CAR_TYPES = {100, 200}
BIKE_TYPES = {610}


def read_link_labels(labels_file):
    """Read Link -> Label mapping from links.txt."""
    labels = {}

    with open(labels_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            # Skip header line, for example: Link  Lable
            if line.lower().startswith("link"):
                continue

            parts = re.split(r"\s+", line)

            if len(parts) >= 2:
                try:
                    link_no = int(parts[0])
                    label = " ".join(parts[1:])
                    labels[link_no] = label
                except ValueError:
                    pass

    return labels


def read_fhz_rows(fhz_file):
    """
    Read vehicle rows from a .fhz file.

    Header lines before the actual data table are ignored.
    The data table is identified by a line beginning with 'Time;'.
    """
    rows = []
    columns = None

    with open(fhz_file, "r", encoding="utf-8", errors="ignore") as f:
        for raw_line in f:
            line = raw_line.strip()

            if not line:
                continue

            # The actual table starts here.
            if line.startswith("Time;"):
                columns = [col.strip() for col in line.split(";") if col.strip()]
                continue

            # Ignore everything before the table header.
            if columns is None:
                continue

            # Ignore non-data lines after the header.
            if ";" not in line:
                continue

            values = [val.strip() for val in line.split(";") if val.strip()]

            if len(values) != len(columns):
                continue

            row = dict(zip(columns, values))
            rows.append(row)

    return rows


def main():
    if len(sys.argv) != 4:
        print("Usage:")
        print("python count_generated_vehicles.py input.fhz links.txt output.txt")
        sys.exit(1)

    fhz_file = sys.argv[1]
    links_file = sys.argv[2]
    output_file = sys.argv[3]

    labels = read_link_labels(links_file)
    rows = read_fhz_rows(fhz_file)

    type_counts = Counter()
    link_counts = Counter()
    link_type_counts = {}

    for row in rows:
        try:
            link_no = int(row["Link"])
            veh_type = int(row["VehType"])
        except (KeyError, ValueError):
            continue

        type_counts[veh_type] += 1
        link_counts[link_no] += 1

        if link_no not in link_type_counts:
            link_type_counts[link_no] = Counter()

        link_type_counts[link_no][veh_type] += 1

    total_all = sum(type_counts.values())
    total_cars = sum(type_counts[t] for t in CAR_TYPES)
    total_bikes = sum(type_counts[t] for t in BIKE_TYPES)

    lines = []
    lines.append("Generated vehicle counts")
    lines.append("------------------------")
    lines.append(f"All: {total_all}")
    lines.append(f"Cars (100, 200): {total_cars}")
    lines.append(f"Bikes (610): {total_bikes}")
    lines.append("")
    lines.append("Links:")
    lines.append("Link   Label       All   Cars   Bikes")

    for link_no in sorted(link_counts):
        label = labels.get(link_no, "-")
        all_count = link_counts[link_no]
        car_count = sum(link_type_counts[link_no][t] for t in CAR_TYPES)
        bike_count = sum(link_type_counts[link_no][t] for t in BIKE_TYPES)

        lines.append(f"{link_no:<6} {label:<10} {all_count:>5} {car_count:>6} {bike_count:>7}")

    output_text = "\n".join(lines)

    # Console output
    print(output_text)

    # File output
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_text)
        f.write("\n")


if __name__ == "__main__":
    main()
