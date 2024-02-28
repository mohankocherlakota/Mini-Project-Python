"""
Assigment-2


Copyright (c) 2021 -- This is the 2021 Spring B version of the Template
Licensed
Written by <> <---- VSN SAI KRISHNA MOHAN KOCHERLAKOTA- ASSIGNMENT_2

# you can also rely on the docstring documentation from pandas on how to format dosctrings:
# https://pandas.pydata.org/pandas-docs/stable/development/contributing_docstring.html

"""
"Neural Dataset"

import csv

file_path = r"C:\Users\kvsns\Downloads\Neural_data.csv"

with open(file_path, newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)

import pandas as pd

def calculate_statistics(csv_file):
    # Read the CSV file into a DataFrame
    data = pd.read_csv(csv_file)

    # Extract the specified columns
    columns_of_interest = [
        'Intensity_MassDisplacement_PI',
        'Intensity_MaxIntensityEdge_DAPI',
        'Intensity_MaxIntensityEdge_PI',
        'Intensity_MaxIntensity_DAPI',
        'Intensity_MaxIntensity_PI',
        # Add the rest of the columns here...
        'Number_Object_Number'
    ]

    # Calculate statistics for the specified columns
    column_stats = data[columns_of_interest].describe()

    return column_stats


# Calculate statistics for specified columns
stats = calculate_statistics(file_path)
"Nested Data"
import json

# Path to your JSON file
file_path = r'C:\Users\kvsns\Downloads\nested_data.json'

# Open the JSON file with UTF-8 encoding and load its contents
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
def calculate_total_mass(data):
    total_mass = 0
    for meteorite in data:
        if 'mass' in meteorite:
            mass = meteorite['mass']
            # Handling cases where mass might not be a number
            try:
                total_mass += float(mass)
            except ValueError:
                print(f"Invalid mass value for meteorite: {meteorite['name']}")
    return total_mass

# Calculate total mass of all meteorites
total_mass = calculate_total_mass(data)

"Network Data"
# Specify the path to your text file
file_path = r'C:\Users\kvsns\Downloads\network_data.txt'

# Open the text file with UTF-8 encoding
with open(file_path, 'r', encoding='utf-8') as file:
    text_data = file.read()

# Splitting the content by lines
lines = text_data.split('|0')

# Extracting device type from each line
def extract_device_types(lines):
    device_types = []

    for line in lines:
        if line:  # Skipping empty lines
            data = line.split('|')
            device_info = data[4]  # Assuming the device info is at index 4
            device_type = device_info.split('|')[0]  # Extracting the device type
            device_types.append(device_type)  # Storing device type in a list

    return device_types
"Excel Report"
import pandas as pd
import matplotlib.pyplot as plt
file_path = r'C:\Users\kvsns\Downloads\Excel_report.xlsx'

# Read a specific sheet named 'Sheet000' from the Excel file
data = pd.read_excel(file_path, sheet_name='Sheet000')

# Read the Excel file
data = pd.read_excel(file_path, sheet_name='Sheet000')

# Drop rows with all NaN values
data.dropna(axis=0, how='all', inplace=True)

# Drop columns with all NaN values
data.dropna(axis=1, how='all', inplace=True)
# Plotting the count of each Segment
segment_counts = data['Unnamed: 2'].value_counts()
segment_counts.plot(kind='bar')
plt.xlabel('Segment')
plt.ylabel('Count')
plt.title('Count of Each Segment')
plt.show()

def function1(var1,var2,var3):
    """
    :param var1: please describe
    :param var2: please describe
    :param var3: please describe
    :return:
    """

    return

def function2(var1,var2,var3):
    """
    :param var1:
    :param var2:
    :param var3:
    :return:
    """

    return

if __name__ == "__Mohan__":
    # Main functions to Run
	function1(var1=123, var2=456, var3=678)

	
