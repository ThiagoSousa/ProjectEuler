######################################################################################################
### Problem 9: There exists exactly one Pythagorean triplet for which a + b + c = 1000.
### Find the product abc.
### Autor: Thiago de Sousa Silveira
######################################################################################################
import math

#Solution 1
for a in range(1000):
	for b in range(a+1,1000):
		c = 1000-a-b
		if c>b and c == math.sqrt(a*a+b*b):
			print a*b*c

#Solucao 2
for a in range(333):
	b = (-1000000+2000*a)/(-2000+2*a)
	c = 1000-a-b
	if b>0 and c>b and c == math.sqrt(a*a+b*b):
		print a*b*c