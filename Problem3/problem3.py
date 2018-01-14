######################################################################################################
### Problem 3: What is the largest prime factor of the number 600.851.475.143 ?
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

#calculate the largest prime factor of n
n = 600851475143
prime = 3
while n!=1:
	if n%prime==0:
		n /= prime
	else:
		prime = next_prime(prime)
print prime