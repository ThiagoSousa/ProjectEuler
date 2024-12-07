# Mathematical solution

# For all the numbers from 1 to 20, we need to find the prime factors of these numbers and multiple the highest power of each prime factor found

# 1: 1
# 2: 2
# 3: 3
# 4: 2^2
# 5: 5
# 6 : 2*3
# 7: 7
# 8: 2^3
# 9: 3^2
# 10: 2*5
# 11: 11
# 12: 2^2*3
# 13: 13
# 14: 2*7
# 15: 3*5
# 16: 2^4
# 17: 17
# 18: 3^2*2
# 19: 19
# 20: 2^2*5

# print(2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19)


# Coding Solution

from utils.prime_functions import next_prime


def prime_factors(n: int) -> dict:
    """
    Finds the prime factors
    :param n: number
    :return: dictionary with the prime factors of the number
    """

    if n == 1:
        return {1: 1}

    prime = 2
    factors = {}

    while n > 1:
        if n % prime == 0:
            n /= prime
            factors[prime] = factors.get(prime, 0) + 1
        else:
            prime = next_prime(prime)
    return factors


def lcm(numbers: list[int]) -> int:
    """
    Find the Least common multiple of a list of numbers
    :param numbers: given list of numbers
    :return: should retun the lcm result
    """

    highest_factors = {}
    for number in numbers:
        factors = prime_factors(number)
        for prime in factors:
            if prime not in highest_factors or factors[prime] > highest_factors[prime]:
                highest_factors[prime] = factors[prime]

    product = 1
    for prime in highest_factors:
        product *= prime**highest_factors[prime]
    return product

print(lcm([i for i in range(1, 21)]))
