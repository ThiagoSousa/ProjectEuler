######################################################################################################
### Problem 6: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
### Autor: Thiago de Sousa Silveira
######################################################################################################

#Solution 1: iteration
sum_squares = 0
square_sum = 0
for i in range(1,101):
	square_sum += i
	sum_squares += i*i
print square_sum*square_sum-sum_squares

#Solution 2: pen and paper
square_sum = (1+100)*100/2
sum_squares = 100*(101)*(2*100+1)/6
print square_sum*square_sum-sum_squares