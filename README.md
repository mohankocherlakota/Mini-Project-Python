# Data Analysis Project

This project involves analyzing various datasets and performing different data processing tasks. Below is an overview of the main components and datasets used in this project.

## Datasets

1. **Neural Dataset** (Neural_data.csv)
   - Contains data related to neural intensity measurements.
   - Analyzed using pandas for statistical calculations.

2. **Nested Data** (nested_data.json)
   - JSON file containing nested data structures.
   - Includes information about meteorites, including their mass.

3. **Network Data** (network_data.txt)
   - Text file containing network-related information.
   - Data is parsed to extract device types.

4. **Excel Report** (Excel_report.xlsx)
   - Excel file with multiple sheets, focusing on 'Sheet000'.
   - Contains segment data for visualization.

5. **Walmart Store Openings** (1962_2006_walmart_store_openings.csv)
   - CSV file with data on Walmart store openings from 1962 to 2006.
   - Includes information such as store numbers, opening dates, and locations.

## Main Features

1. **Neural Data Analysis**
   - Calculates statistics for specified columns in the neural dataset.
   - Uses pandas for data manipulation and analysis.

2. **Meteorite Mass Calculation**
   - Processes nested JSON data to calculate the total mass of meteorites.
   - Handles potential errors in mass values.

3. **Network Device Type Extraction**
   - Parses network data to extract and categorize device types.

4. **Excel Data Visualization**
   - Reads Excel data, cleans it by removing NaN values.
   - Creates a bar plot showing the count of each segment.

5. **Walmart Store Analysis**
   - Imports and analyzes Walmart store opening data.
   - Performs various data manipulations and calculations, including:
     - Identifying states with the highest number of Walmart super stores.
     - Finding cities with the highest total number of Walmart stores.
     - Creating time series of cumulative store counts for specific states.

## Python Scripts

1. **Template.py**
   - Contains functions for processing neural data, nested data, network data, and Excel reports.
   - Includes placeholder functions for further development.

2. **Module_4_Assignment.ipynb**
   - Jupyter notebook focusing on the Walmart store opening dataset.
   - Includes data import, cleaning, and analysis tasks.

3. **Module_3_Assignment_Kocherlakota.ipynb** and **Module_1_Assignment.ipynb**
   - Additional Jupyter notebooks with various data processing and analysis tasks.

## Requirements

- Python 3.x
- Libraries: pandas, numpy, matplotlib, json, csv

## Usage

1. Ensure all required datasets are in the correct file paths.
2. Run the Python scripts or Jupyter notebooks as needed for specific analyses.
3. Modify the file paths in the scripts if the data files are located differently on your system.

## Note

This project is a collection of various data analysis tasks and may require further integration or structuring depending on specific use cases or requirements.

