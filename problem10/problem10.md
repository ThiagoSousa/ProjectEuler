# Problem 10

## Solution 1

We use the next_prime function to start from 2 and until we reach 2 million, to summing the primes we find in the way. 
Complexity: O(sqrt(n)*n)

## Solution 2:
We implement the [Sieve of Erastothenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) to reduce the search space. 