######################################################################################################
### Problem 10: Find the sum of all the primes below two million.
### Autor: Thiago de Sousa Silveira
######################################################################################################
import math

#chech if n is prime
def is_prime(n):
	if n<=1:
		return False
	if n==2:
		return True
	if n%2==0:
		return False
	for i in range(3,int(math.sqrt(n))+1,2):
		if n%i==0:
			return False
	return True

#return next prime
def next_prime(n):
	n+=1
	while not is_prime(n):
		n+=1
	return n

#calculate sum of primes
p = 2
s = 0
while p<2000000:
	s += p
	p = next_prime(p)
print s