
# Coding

sum_squares = 0
square_sums = 0
for i in range(1, 101):
    sum_squares += i**2
    square_sums += i

print(square_sums**2 - sum_squares)

# Mathematical Solution
# sum of squares: Sn = n*(n+1)*(2*n+1)/6
# Sum of sequence = Sn = (a1+an)*n/2

n = 100
sum_squares = int(n*(n+1)*(2*n+1)/6)
square_sums = int(((1+100)*100/2)**2)

print(square_sums-sum_squares)