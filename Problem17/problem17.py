######################################################################################################
### Problem 17: If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
### how many letters would be used?
### Autor: Thiago de Sousa Silveira
######################################################################################################

numbers = dict()
numbers[1] = "one"
numbers[2] = "two"
numbers[3] = "three"
numbers[4] = "four"
numbers[5] = "five"
numbers[6] = "six"
numbers[7] = "seven"
numbers[8] = "eight"
numbers[9] = "nine"
numbers[10] = "ten"
numbers[11] = "eleven"
numbers[12] = "twelve"
numbers[13] = "thirteen"
numbers[14] = "fourteen"
numbers[15] = "fifteen"
numbers[16] = "sixteen"
numbers[17] = "seventeen"
numbers[18] = "eighteen"
numbers[19] = "nineteen"

numbers_tens = dict()
numbers_tens[2] = "twenty"
numbers_tens[3] = "thirty"
numbers_tens[4] = "forty"
numbers_tens[5] = "fifty"
numbers_tens[6] = "sixty"
numbers_tens[7] = "seventy"
numbers_tens[8] = "eighty"
numbers_tens[9] = "ninety"

#summing the letters of numbers from 1-1000
s = 0
for i in range(1,1000):
    hundreds = i/100
    unit = i%100
    if hundreds>0:
        s += len(numbers[hundreds])+len("hundred")
        if unit>0:
            s+=3

    if unit<20 and unit>0:
        s+= len(numbers[unit])
    elif unit>0:
        tens = unit/10
        unit = unit%10
        s += len(numbers_tens[tens])
        if unit>0:
            s+= len(numbers[unit])
s+=len("onethousand")
print s