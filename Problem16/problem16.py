######################################################################################################
### Problem 16: What is the sum of the digits of the number 21000?
### Autor: Thiago de Sousa Silveira
######################################################################################################

#Solucao 1
print sum([int(i) for i in str(2**1000)])








#Solution 2
class BigInt():

    #init
    def __init__(self, number):
        self.number = []
        for i in number:
            self.number += [int(i)]

    #adding function
    def mult(self, othernumber):
        result = BigInt("0")
        result_i = 0 
        for i in range(len(othernumber.number)-1,-1,-1):
            n2 = othernumber.get_digit(i)
            remainder = 0
            result_j = 0 
            for j in range(len(self.number)-1,-1,-1):
                n1 = self.get_digit(j)
                s = n1*n2 + result.get_digit(result_i+result_j) + remainder
                remainder = s/10
                result.put(result_i+result_j,s%10)
                result_j += 1
            if remainder>0:
                result.put(result_i+result_j,remainder)
            result_i += 1
        result.number.reverse()
        self.number = result.number

    def get_digit(self,i):
        if i>=len(self.number):
            return 0
        return self.number[i]

    def put(self, i, v):
        if i>=len(self.number):
            self.number += [v]
        else:
            self.number[i] = v

    def to_print(self):
        print self.number

number = BigInt("2")
for i in range(999):
    number.mult(BigInt("2"))
print sum(number.number)