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