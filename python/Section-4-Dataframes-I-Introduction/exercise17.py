# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work
import pandas as pd 

# This challenge's dataset (switch_games.csv) is a collection of video games
# released on Nintendo's Switch gaming system.
# It has 5 columns: Title, Genre, Developer, Publisher, and Release date
# Import the DataFrame from the CSV and assign it to a "games" variable
games = pd.read_csv("switch_games.csv")

# Extract the "Title" and "Developer" columns to a new DataFrame.
# Assign the DataFrame to a "name_and_maker" variable.
name_and_maker = games[["Title", "Developer"]]

# Extract the "Genre" and "Publisher" columns to a new DataFrame.
# Assign the DataFrame to a "genre_and_publisher" variable.
genre_and_publisher = games[["Genre", "Publisher"]]

# Extract the "Title", "Genre", and "Publisher" columns to a new DataFrame.
# Assign the DataFrame to a "metadata" variable.
metadata = games[["Title", "Genre", "Publisher"]]