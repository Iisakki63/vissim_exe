# -*- coding: utf-8 -*-
import pandas as pd
import re
import sys

def read_vissim_rsr(filepath):
    with open(filepath, 'r') as file:
        content = file.read()

    # Extract the table
    table_data = re.search(r"Time;.+\n(.+\n)+", content).group()
    lines = table_data.splitlines()

    # Clean column names
    columns = [col.strip().replace('.', '') for col in lines[0].split(';') if col.strip()]
    
    # Read data
    data = []
    for line in lines[1:]:
        if line.strip():
            values = [float(val.strip()) for val in line.split(';') if val.strip()]
            data.append(values)

    df = pd.DataFrame(data, columns=columns)
    return df


# Main program

# for i, arg in enumerate(sys.argv[1:], start=1):
    # print(f"Argument {i}:", arg)

print(f"\nAverage delay calculation for Vissim (2025)")

inpfilepath = 'testxx.rsr'
inpfilepath = sys.argv[1]
df = read_vissim_rsr(inpfilepath)
print("Input path/file: ", inpfilepath)

outfilepath = 'testxx.rsr'
outfilepath = sys.argv[2]
print("Output path/file: ", outfilepath)


# Group by road number
grouped = df.groupby("No")

# Total counts = count of entries
total_vehicles = grouped.size().reset_index(name="Total counts")

# Average delay, rounded to 1 decimal
average_delays = grouped["Delay"].mean().round(1).reset_index(name="Average Delay")

# Merge both
summary = pd.merge(total_vehicles, average_delays, on="No")

# Reorder columns
summary = summary[["No", "Total counts", "Average Delay"]]

# Add summary lines
total_avg_delay = df["Delay"].mean()
total_vehs = 1000   # How to get the correct value ?

main_road_avg = df[df["No"].between(1, 4)]["Delay"].mean()
main_count = 400  #  df[df["No"].between(11, 14)].... How to ?

side_road_avg = df[df["No"].between(11, 14)]["Delay"].mean()
side_count = 200  #  df[df["No"].between(11, 14)].... How to ?

car_avg = df[df["No"].between(1, 14)]["Delay"].mean()
car_count = 800  # df[df["No"].between(21, 22)].... How to ?

biker_avg = df[df["No"].between(21, 22)]["Delay"].mean()
biker_count = 100  # df[df["No"].between(21, 22)].... How to ?

print(f"Altogether: Count: {total_vehs} Average delay: {total_avg_delay:.1f}")

print(f"Main roads (1-4): Count: {main_count} Average delay:  {main_road_avg:.1f}")

print(f"Side roads (11–14): Count: {side_count} Average delay:  {side_road_avg:.1f}")

print(f"Cars (1–14): Count: {car_count} Average delay: {car_avg:.1f}")

print(f"Bikers (21–22): Count: {biker_count} Average delay: {biker_avg:.1f}")

# Print table
print('Travel time elements:')
print(summary.to_string(index=False))

# File output
# outfilepath = 'test.del'
# print('outfile: ', outfilepath)
f = open(outfilepath, "w")

f.write(str(f"Average delay calculation for Vissim (2025)"))
f.write(str(f"\nAltogether: Count: {total_vehs} Average delay: {total_avg_delay:.1f}"))
f.write(str(f"\nMain roads (1-4): Count: {main_count} Average delay:  {main_road_avg:.1f}"))
f.write(str(f"\nSide roads (11-14): Count: {side_count} Average delay:  {side_road_avg:.1f}"))
f.write(str(f"\nCars (1-14): Count: {car_count} Average delay: {car_avg:.1f}"))
f.write(str(f"\nBikers (21-22): Count: {biker_count} Average delay: {biker_avg:.1f}"))
f.write(str(f"\nTravel time elements:"))
# Print table
f.write('\n')
f.write(str(summary))

f.close()

