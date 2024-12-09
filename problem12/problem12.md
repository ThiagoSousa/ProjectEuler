# Problem 12

## Solution 

We implement a function `get_divisors` to get the list of divisors of a number. I implemented it as a set, but it can 
be a list. I check divisors from 2->sqrt(n) adding the remainder of division and the quotient itself.

I implemented also a function `number_divisors` that simply returns the number of divisors, by calling `get_divisors` and 
returning the size of the resulting vector. 

To find the triangular numbers, I implemented two methods: 

1. Iterated through the triangular number sequence starting from 1 and getting the next one by summing the iterator int.
2. Used a formula for triangular number: $T(n) = (n*(n+1)/2)$

Why is T(n) the formula for the triangular number sequence?

Proof by induction:

T(1) = 1*(1+1)/2 = 1*2/2 = 1
T(k) = k*(k+1)/2

Inductive step:
T(k+1) = (k+1)*(k+1+1)/2 = (k+1)*(k+2)/2 = (k^2+2k+k+2)/2

Reorganizing it:
T(k+1) = (k(k+1)+2(k+1))/2 = k(k+1)/2 + 2(k+1))/2 = k(k+1)/2 + (k+1)

Since T(k) = k*(k+1)/2, then:
T(k+1) = T(k)+(k+1)

And this is the inductive step proof for this formula.