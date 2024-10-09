import pandas as pd

"""
Problem 4: Alert Script

This script will loop through the data and will alert
when:

*The water level increases more than 0.25 since the previous recording.
*The water level is over 5.0.
*No reading is received at a time point.

"""

# Load the data
file_path = r"C:\Manuel\UF\Plant_breeding_PhD\semester 9 fall 2024\BSC6451 Computational Tools for Research in Biology\assignments\Problem_Set_3\CO-OPS__8729108__wl.csv"
data = pd.read_csv(file_path)

# Strip any leading/trailing spaces from column names
data.columns = data.columns.str.strip()

# Print the column names to verify them
print("Column names:", data.columns.tolist())

# Loop through the data to check for missing values
for i in range(len(data)):
    # Check for missing readings
    if pd.isnull(data['Water Level'][i]):
        print(f"Missing value at {data['Date Time'][i]}!")

# Loop through the data to check conditions
for i in range(1, len(data)):
    # Calculate the change in water level
    change = data['Water Level'][i] - data['Water Level'][i-1]
    
    # Check for water level increase
    if change > 0.25:
        print(f"Warning: Rapid increase in water level detected at {data['Date Time'][i]}! Change: {change:.2f} ft, Current Level: {data['Water Level'][i]:.2f} ft")

    # Check for water level over 5.0
    if data['Water Level'][i] > 5.0:
        print(f"Warning: Water level exceeds 5.0 at {data['Date Time'][i]}! Current Level: {data['Water Level'][i]:.2f} ft")
