import datetime

start_time = datetime.datetime.now()
threshold = 4000000
s = 0
a = 1
b = 2

while b < threshold:
    if b % 2 == 0:
        s += b
    aux = a+b
    a = b
    b = aux

print(s)
print(f"Time: {datetime.datetime.now()-start_time}")


# Solution 2
# 1,2,3,5,8,13,21,34,....
# an = 4*an-1 + an-2
start_time = datetime.datetime.now()
threshold = 4000000
s = 2
a = 2
b = 8
while b < threshold:
    s += b
    aux = 4*b+a
    a = b
    b = aux
print(s)
print(f"Time: {datetime.datetime.now()-start_time}")
