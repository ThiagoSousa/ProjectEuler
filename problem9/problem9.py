import datetime

# a+b+c = 1000 and a^2+b^2 = c^2 and a<b<c


def pythagorean_triplet(a: int, b: int, c: int) -> bool:
    """
    Check if a,b and c are a pythagorean triplet
    :param a:
    :param b:
    :param c:
    :return: true or false for the check
    """

    return a**2+b**2 == c**2

# Solution 1: time complexity O(n^3)
start_time = datetime.datetime.now()
for a in range(1000):
    for b in range(a+1, 1000):
        for c in range(b+1, 1000):
            if a+b+c == 1000 and pythagorean_triplet(a,b,c):
                print(a, b, c, a*b*c)
                break
print(f"Time {datetime.datetime.now()-start_time}")


# Solution 2: time complexity O(n^2)
start_time = datetime.datetime.now()
for a in range(1000):
    for b in range(a+1, 1000):
        c = 1000-a-b
        if pythagorean_triplet(a,b,c):
            print(a, b, c, a * b * c)
            break
print(f"Time {datetime.datetime.now()-start_time}")

# Solution 3: time complexity O(n)
# a+b+c == 1000
# a^2+b^2 == c^2
# c = 1000-a-b
# pluging in c into a^2+b^2 == c^2, we have:
# a^2+b^2 = (1000-a-b)^2
# a^2+b^2 = 1000^2 + a^2 +b^2 + 2*1000*a +2*1000*b + 2ab
# a^2+b^2 = 1000^2 + a^2 +b^2 + 2000*a +2000*b + 2ab cancel a^2+b^2 from both sides
# 0 = 1000^2 + 2000*a +2000*b + 2ab
# 2ab = 2000*a +2000*b - 1000^2
# 2ab - 2000*b = 2000*a - 1000^2
# b(2a-2000) = 2000*a - 1000^2
# b = (2000*a - 1000^2)/(2a-2000)

start_time = datetime.datetime.now()
for a in range(1, 1000):
    b = int((2000*a - 1000000)/(2*a-2000))
    c = 1000-a-b
    if pythagorean_triplet(a, b, c):
        print(a, b, c, a * b * c)
        break
print(f"Time {datetime.datetime.now() - start_time}")