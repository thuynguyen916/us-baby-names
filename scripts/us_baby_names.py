# Project: US Baby Name Popularity from 2020 to 2023
# Analyst: Thuy Nguyen (individually done)

import os
import pandas as pd

# Use the current folder that this .py file is saved in
folder_path = '.'

# Create a list of all .txt files, which they all start with yob

all_files = []
for file in os.listdir(folder_path):
    if file.startswith('yob') and file.endswith('.txt'):
        all_files.append(file)

combined_data = []

# Iterate over all the files
for file in all_files:
    year = int(file[3:7]) # Only 4 digit of the year
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path, names = ['Name', 'Sex', 'Count'])
    df['Year'] = year # Add Year column
    combined_data.append(df)

# Merge all yearly dataframes into one
final_df = pd.concat(combined_data)

# Save the result to a csv file
final_df.to_csv('us_baby_names.csv', index = False)

print("CSV file 'us_baby_names.csv' has been created.")
