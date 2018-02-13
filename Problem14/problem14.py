######################################################################################################
### Problem 13: Which starting number, under one million, produces the longest chain?
### Autor: Thiago de Sousa Silveira
######################################################################################################
import operator

#Solution 1
maxchain = 0
maxchain_number = 0
chain = dict()
chain[1] = 1
for i in range(1000000,0,-1):
	n = i
	cont = 1
	while n!=1:
		if n not in chain:
			if n%2==0:
				n /= 2
			else:
				n = 3*n+1
			cont += 1
		else:
			cont += chain[n]
			break
	chain[i] = cont
	if cont>maxchain:
		maxchain = cont
		maxchain_number = i
print maxchain_number

#Solution 2
def chain_length(n):
	if n not in chain:
		if n%2==0:
			chain[n] = chain_length(n/2) + 1
		else:
			chain[n] = chain_length(3*n+1) + 1
	return chain[n]

chain = dict()
chain[1] = 1
for i in range(1000000,0,-1):
	chain_length(i)
print max(chain.iteritems(), key=operator.itemgetter(1))[0]