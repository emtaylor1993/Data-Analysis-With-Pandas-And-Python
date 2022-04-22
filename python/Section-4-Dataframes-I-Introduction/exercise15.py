# The data.csv file contains a dataset of random numbers.
# Import pandas and use it to parse the CSV.
# Assign the imported DataFrame to a variable called 'data'.
import pandas as pd
data = pd.read_csv("data.csv")

# The dataset has 4 columns: A, B, C, and D.
# Filter the dataset to remove rows that have a missing value
# in either the "B" or "D" columns.
# Assign the resulting DataFrame to a "result" variable.
result = data.dropna(subset = ["B", "D"])