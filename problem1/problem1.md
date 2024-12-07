
# Problem 1

## Solution 1

We just iterate through the numbers below 1000 and sum the numbers divisible by 3 or 5.

## Solution 2

Use the sum of sequences to sum the multiples of 3, 5 and subtract the numbers that are multiple of both. 

* Multiples of 3: 3,6,9,12,15,....

* Multiple of 5: 5,10,15,20,...

* Multiple of 15: 15,30,45,...

`Sn = ((a1 + an)*n)/2`

`sn = int((3+999)*(int(1000/3))/2 + (5+995)*(1000/5-1)/2 - (15+990)*(int(1000/15))/2)`