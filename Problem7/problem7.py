######################################################################################################
### Problem 7: What is the 10001st prime number?
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

#find the 10001th prime
p=2
for i in range(1,10001):
	p = next_prime(p)
print p