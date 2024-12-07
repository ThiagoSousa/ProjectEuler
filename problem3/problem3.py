import datetime
import math


def is_prime(n: int) -> bool:
    """
    Check if a number is prime. O(sqrt(n))
    :param n: number
    :return: True or False
    """

    if n < 2:
        return False

    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def next_prime(n: int) -> int:
    """
    Generate the next prime given an integer
    :param n: number
    :return: next larger prime than number n
    """

    n = n + 1
    while not is_prime(n):
        n += 1
    return n

start_time = datetime.datetime.now()
number = 600851475143
largest_prime = 0
prime = 2
while number > 1:
    if number % prime == 0:
        number = number / prime
        largest_prime = prime
    else:
        prime = next_prime(prime)
print(largest_prime)
print(f"Time: {datetime.datetime.now()-start_time}")