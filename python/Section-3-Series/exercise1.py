###############################################################
# DO NOT DELETE THIS CODE. IT IS NEEDED FOR THE TESTS TO RUN. #

from unittest.mock import MagicMock
import pandas as pd
pd.Series = MagicMock()

###############################################################

# Assume the pandas library has already been imported and assigned
# the alias "pd"

# Create a list with 4 countries - United States, France, Germany,
# Italy. Create a new Series by passing in the list of coutnries
# Assign the Series to a "countries" variable

country_list = ['United States', 'France', 'Germany', 'Italy']
countries = pd.Series(country_list)

# Create a list with 3 colors - red, green, blue. Create a new
# Series by passing in the list of colors. Assign the Series to a
# "colors" variable.

color_list = ['red', 'green', 'blue']
colors = pd.Series(color_list)

# Given the "recipe" dictionary below, create a new Series by passing
# in the dictionary as the data source. Assign the resulting series
# to a "series_dict" variable

recipe = {
	"Flour" : True,
	"Sugar" : True,
	"Salt" : False
}

series_dict = pd.Series(recipe)