letters_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
                10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
                17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
                60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}


def count_letters_number(n: int) -> int:
    """
    Count the number of letters a number has
    :param n: given number
    :return: total number of letters
    """

    if n == 1000:
        return len("onethousand")

    number_string = ""

    if n >= 100:
        hundreds = n // 100
        n = n % 100
        number_string += letters_dict[hundreds]+"hundred"
        if n > 0:
            number_string += "and"
    if n > 20:
        tens = n // 10
        n = n % 10
        number_string += letters_dict[tens*10]

    if n > 0:
        number_string += letters_dict[n]

    return len(number_string)


print(sum([count_letters_number(i) for i in range(1, 1001)]))
