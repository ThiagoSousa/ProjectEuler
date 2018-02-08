######################################################################################################
### Problem 12: What is the value of the first triangle number to have over five hundred divisors?
### Autor: Thiago de Sousa Silveira
######################################################################################################
import math

#calculate the number of divisors.
def cont_divisors(n):
	if n==1:
		return 1
	cont = 0
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			cont += 2
	return cont+2

#expand the sequence of triangular numbers
cont = 1
n = 1
while cont_divisors(n)<=500:
	cont += 1
	n+=cont
print n