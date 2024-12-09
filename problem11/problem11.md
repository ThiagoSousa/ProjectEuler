
# Problem 11

## Solution

We iterate through the matrix in four different ways to find all 4 adjascent numbers:

* Horizontally: We iterate through all rows and up to column 17 to get the horizontal adjascent sets of 4 numbers
* Vertically: We iterate through all columns and up to row 17.
* Diagonal: We iterate from row and column 1 all the way to row and column 17 to get the diagonals to the right. 
* Anti-Diagonal: We start iterating the rows from column 4 all the way to 20 and from row 0 to 17 to get the anti diagonal.

For each adjacent set of 4 numbers we calculate their product and check if it is the largest.