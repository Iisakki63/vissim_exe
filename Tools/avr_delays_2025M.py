# -*- coding: utf-8 -*-
import pandas as pd
import re

def read_vissim_rsr(filepath):
    with open(filepath, 'r') as file:
        content = file.read()

    table_data = re.search(r"Time;.+\n(.+\n)+", content).group()
    lines = table_data.splitlines()

    # Normalize column names
    columns = [col.strip().replace('.', '') for col in lines[0].split(';') if col.strip()]
    data = []
    for line in lines[1:]:
        if line.strip():
            values = [float(val.strip()) for val in line.split(';') if val.strip()]
            data.append(values)

    df = pd.DataFrame(data, columns=columns)
    return df

filepath = '2junc3phase_VAP3_004.rsr'
df = read_vissim_rsr(filepath)

# Group and compute
grouped = df.groupby("No")
total_vehicles = grouped.size().reset_index(name="Total Vehicles")
average_delays = grouped["Delay"].mean().round(1).reset_index(name="Average Delay")

# Merge
summary = pd.merge(total_vehicles, average_delays, on="No")
summary = summary[["No", "Total Vehicles", "Average Delay"]]
print(summary.to_string(index=False))

# Final summary lines with counts
total_avg_delay = df["Delay"].mean()
total_count = len(df)

side_road_df = df[df["No"].between(11, 14)]
side_road_avg = side_road_df["Delay"].mean()
side_road_count = len(side_road_df)

biker_df = df[df["No"].between(21, 22)]
biker_avg = biker_df["Delay"].mean()
biker_count = len(biker_df)

print(f"\nTotal average delay: {total_avg_delay:.1f} ({total_count} vehicles)")
print(f"Average delay of side roads (11–14): {side_road_avg:.1f} ({side_road_count} vehicles)")
print(f"Average delay of bikers (21–22): {biker_avg:.1f} ({biker_count} vehicles)")
