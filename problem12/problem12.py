import math


def get_divisors(n: int) -> set:
    """
    Get the divisors of a number
    :param n: input number
    :return: set of divisors of n
    """

    divisors = {1, n}

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return divisors


def number_divisors(n: int) -> int:
    """
    Get the total number of divisors of a given number
    :param n: input n
    :return: number of divisors
    """

    return len(get_divisors(n))


def triangular(n: int) -> int:
    """
    Get the nth triangular number
    :param n: position in the sequence
    :return: triangular number
    """

    return int((n*(n+1))/2)

# Solution 1
# n = 1
# i = 1
# while number_divisors(n) <= 500:
#     i += 1
#     n += i
# print(n)

# Solution 2 using the triangular function
i = 1
while number_divisors(triangular(i)) <= 500:
    i += 1
print(triangular(i))
