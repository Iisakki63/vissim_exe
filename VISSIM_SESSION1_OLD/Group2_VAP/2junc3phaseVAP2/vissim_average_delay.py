# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:41:48 2024

@author: bayrakm1
"""

import pandas as pd
import re

def read_vissim_rsr(filepath):
    # Read the file content
    with open(filepath, 'r') as file:
        content = file.read()

    # Extract the table part from the content
    table_data = re.search(r"Time;.+\n(.+\n)+", content).group()

    # Split the table data into lines
    lines = table_data.splitlines()
    # print('Lines: ', lines) 

    # Extract column names from the first line
    columns = [col.strip() for col in lines[0].split(';') if col.strip()]
    print('Columns: ', columns)

    # Extract data rows
    data = []
    for line in lines[1:]:
        if line.strip():
            values = [float(val.strip()) for val in line.split(';') if val.strip()]
            data.append(values)
    # print('Data: ', data)
    
    # Create a pandas DataFrame
    df = pd.DataFrame(data, columns=columns)

    return df

# filepath = 'd:\AALTO\VISSIM_EDU\TM2024_SimExe\VISSIM_EXE_2024\VISSIM_MODELS2\Group1_FIXED\2junc2phaseFIX\out\2junc2phaseFIX_A_001.rsr'

infile = '2junc3phaseVAP_B2_001'
infilepath = 'out/' + infile + '.rsr'

df = read_vissim_rsr(infilepath)
print('DF: ', df)

# Calculate the average delay for each unique "No." value
average_delays = df.groupby("No.")['Delay.'].mean().reset_index()

# Rename the columns
average_delays.columns = ["No.", "Average Delay"]

print(average_delays)

outfilepath = 'out/' + infile + '.del'

print('outfile: ', outfilepath)

f = open(outfilepath, "w")
f.write(str(average_delays))
f.close()

