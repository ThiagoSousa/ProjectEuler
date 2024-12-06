
# Solution 1

s = 0
for i in range(1000):
    if i%3==0 or i%5==0:
        s += i
print(s)

# Solution 2: Mathematical solution
# multiples of 3: 3,6,9,12,15,....
# multiple of 5: 5,10,15,20,...
# multiple of 15: 15,30,45,...

# Sn = ((a1 + an)*n)/2

sn = int((3+999)*(int(1000/3))/2 + (5+995)*(1000/5-1)/2 - (15+990)*(int(1000/15))/2)
print(sn)