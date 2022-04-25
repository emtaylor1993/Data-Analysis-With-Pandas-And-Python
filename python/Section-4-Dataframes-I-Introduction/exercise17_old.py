###############################################################
# DO NOT DELETE THIS CODE. IT IS NEEDED FOR THE TESTS TO RUN. #
from ignore import df                                         #
###############################################################

# Assume the pandas library has already been imported and assigned an alias of 'pd'.
# Let's say I have a DataFrame that looks like this:
#
#     A	  B	  C	  D	  E
#  0  7	  8	  9	  7	  5
#  1  7	  5	  3	  6	  9
#  2  3	  8	  8	  4	  4
#
# The DataFrame has been assigned to the variable "df"

# Write the code to extract the "C" and "D" columns from the DataFrame (in that order).
select = ["C", "D"]
df[select]

# Write the code to extract the "E" and "B" columns from the DataFrame (in that order).
select = ["E", "B"]
df[select]

# Write the code to extract the "C", "D", "A" columns from the DataFrame (in that order).
select = ["C", "D", "A"]
df[select]

# Write the code to extract the columns in reverse order (E through A) from the DataFrame
select = ["E", "D", "C", "B", "A"]
df[select]