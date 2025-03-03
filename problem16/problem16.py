
# solution 1
print(sum([int(i) for i in str(2**1000)]))


def power_digit_sum(n: int, power:int) -> int:
    """
    Calculate the sum of the digits of n^p
    :param n: number
    :param power: power
    :return: the sum of the digits
    """

    digits = [1]
    for i in range(power):
        carry = 0
        for j in range(len(digits)):
            digit = digits[j] * 2 + carry
            digits[j] = digit % 10
            carry = digit // 10
        if carry >0:
            digits.append(carry)
    return sum(digits)

print(power_digit_sum(2, 1000))