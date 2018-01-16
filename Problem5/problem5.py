######################################################################################################
### Problem 5: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
### Autor: Thiago de Sousa Silveira
######################################################################################################

def is_divisible(n):
	if n%19!=0 or n%18!=0 or n%17!=0 or n%16!=0 or n%15!=0 or n%14!=0 or n%13!=0 or n%12!=0 or n%11!=0:
		return False
	return True

n = 40
while not is_divisible(n):
	n += 20
print n