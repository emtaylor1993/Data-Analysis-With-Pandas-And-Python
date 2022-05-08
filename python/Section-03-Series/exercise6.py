import pandas as pd

# Below, we have a list of delicious tortilla chip flavors
flavors = ["Spicy Sweet Chili", "Cool Ranch", "Nacho Cheese", "Salsa Verde"]

# Create a new Series object, passing in the flavors list defined above
# Assign it to a 'doritos' variable. The resulting Series should look like this:
#
#
#   0    Spicy Sweet Chili
#   1           Cool Ranch
#   2         Nacho Cheese
#   3          Salsa Verde
#   dtype: object
doritos = pd.Series(flavors)

# Below, sort the doritos Series in descending order.
# Make sure the operation is permanent.
# The Series should like this afterwards:
#
#   0    Spicy Sweet Chili
#   3          Salsa Verde
#   2         Nacho Cheese
#   1           Cool Ranch
#   dtype: object
doritos.sort_values(ascending = False, inplace = True)