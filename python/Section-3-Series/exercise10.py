# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work
import pandas as pd

# This challenge includes a coffee.csv with 2 columns: 
# Coffee and Calories. Import the CSV. Assign the Coffee
# column to be the index and the Calories column to be the
# Series' values. Assign the Series to a 'coffee' variable.
coffee = pd.read_csv("coffee.csv", index_col = "Coffee").squeeze("columns")

# Check whether the coffee 'Flat White' is present in the data.
# Assign the result to a `flat_white` variable
flat_white = "Flat White" in coffee.index

# Check whether the coffee 'Cortado' is present in the data.
# Assign the result to a `cortado` variable
cortado = "Cortado" in coffee.index

# Check whether the coffee 'Blackberry Mocha' is present in the data.
# Assign the result to a `blackberry_mocha` variable
blackberry_mocha = "Blackberry Mocha" in coffee.index

# Check whether the value 221 is present in the data.
# Assign the result to a 'high_calorie' variable.
high_calorie = 221 in coffee.values

# Check whether the value 400 is present in the data.
# Assign the result to a 'super_high_calorie' variable.
super_high_calorie = 400 in coffee.values