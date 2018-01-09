######################################################################################################
### Problem 1: Find the sum of natural numbers less than a 1000 which are multiples of 3 or 5.
### Autor: Thiago de Sousa Silveira
######################################################################################################

# Solution 1: brute force
s = 0
for i in range(1,1000):
	if i%3==0 or i%5==0:
		s += i
print s

# Solution 2: list comprehension
print sum([i for i in range(1,1000) if i%3==0 or i%5==0])

# Solucao 3: use sequences, you can do it on paper
s3 = ((3+999)*(999/3))/2
s5 = ((5+995)*(995/5))/2
s15 = ((15+990)*(990/15))/2
print s3+s5-s15