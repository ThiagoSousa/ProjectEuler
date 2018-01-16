######################################################################################################
### Problem 4: Find the largest palindrome made from the product of two 3-digit numbers.
### Autor: Thiago de Sousa Silveira
######################################################################################################

#check if it is a palindrome
def is_palindrome(n):
	n = str(n)
	for i in range(len(n)/2):
		if n[i]!=n[len(n)-1-i]:
			return False
	return True

#make the check in all the 3-digit numbers
max_palindrome = 0
for i in range(100,1000):
	for j in range(100,1000):
		n = i*j
		if n>max_palindrome and is_palindrome(n):
			max_palindrome = n
print max_palindrome