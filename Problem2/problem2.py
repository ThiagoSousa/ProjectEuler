######################################################################################################
### Problem 2: By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
### find the sum of the even-valued terms.
### Autor: Thiago de Sousa Silveira
######################################################################################################

#fibonacci
previous = 1
next = 2
s = 2
while next<4000000:
	aux = next
	next = next+previous
	previous = aux
	if next%2==0:
		s += next
print s
