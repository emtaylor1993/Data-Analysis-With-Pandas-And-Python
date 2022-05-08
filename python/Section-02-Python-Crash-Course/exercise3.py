# Coding Exercise 3: Custom Functions

# Define an easy_money function that accepts no parameters and always returns the value 100
def easy_money():
	return 100
	
# Define a best_food_ever function that accepts no parameters and always returns
# the string "Sushi"
def best_food_ever():
	return "Sushi"
	
# Define a convert_to_currency function that accepts a single parameter (an integer)
# The function should convert the argument to a string, prefix it with a dollar sign, and
# return the results.
def convert_to_currency(currency):
	string = "$" + str(currency)
	return string