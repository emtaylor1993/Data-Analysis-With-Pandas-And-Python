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

# Write the code to sort the DataFrame by the values in the "B" column
# Make sure to explicitly specify that the sort order should be ascending.
df.sort_values("B", ascending = True)

# Write the code to sort the DataFrame by the values in the "D" column
# Make sure to explicitly specify that the sort order should be descending.
df.sort_values("D", ascending = False)

# Write the code to sort the DataFrame first by the values in the "A" column,
# then by the values in the "E" column. The values in "A" should be sorted
# in ascending order while the values in "E" should be sorted in descending order.
df.sort_values(["A", "E"], ascending = [True, False])