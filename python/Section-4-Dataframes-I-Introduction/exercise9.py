# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work
import pandas as pd 

# This challenge includes a "chicken_restaurants.csv" dataset with 6 columns:
# Name, Original Location, Year, Headquarters, Locations, Areas Served
# Import the CSV into a DataFrame and assign it to a "chicken" variable.
chicken = pd.read_csv("chicken_restaurants.csv")

# Extract the "Year" and "Locations" columns (in that order) into
# their own DataFrame. Assign the DataFrame to a "years_and_locations" variable.
years_and_locations = chicken[["Year", "Locations"]]

# Extract the "Locations", "Name", and "Headquarters" columns (in that order)
# into their own DataFrame. Assign the DataFrame to a 
# "interesting_facts" variable.
interesting_facts = chicken[["Locations", "Name", "Headquarters"]]
