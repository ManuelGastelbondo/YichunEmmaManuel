import pandas as pd

"""
Problem Set 3
Question 3: Water Level Analysis

This script finds the fastest rise in water level observed over 
6-minute intervals from the water level observations at Cedar Key. 
It reads the water level data from the CSV file, computes the change 
in water level, and identifies the date and time of the maximum 
rise along with the corresponding change in water level.
"""

# Load the data
# Change the file_path to the correct location of your CSV file
file_path = r"C:\Manuel\UF\Plant_breeding_PhD\semester 9 fall 2024\BSC6451 Computational Tools for Research in Biology\assignments\Problem_Set_3\CO-OPS__8729108__wl.csv"
data = pd.read_csv(file_path)

# Rename the columns for easier access
data.columns = ['DateTime', 'WaterLevel', 'Sigma', 'O', 'F', 'R', 'L', 'Quality']

# Convert the 'DateTime' column to a pandas datetime object
data['DateTime'] = pd.to_datetime(data['DateTime'])

# Calculate the change in water level between each reading
#The .diff() is a panda function that calculates the difference between adjacent
#values in the WaterLevel column
data['Change'] = data['WaterLevel'].diff()

# Find the maximum change (fastest rise) and its corresponding date and time
max_rise_index = data['Change'].idxmax()  # Get the index of the max rise
max_rise_value = data['Change'].max()      # Get the value of the max rise

# Get the date and time of the maximum rise
max_rise_time = data.loc[max_rise_index, 'DateTime']

# Output the results
print(f"The fastest rise in water level occurred on {max_rise_time} with a change of {max_rise_value:.3f} .")
