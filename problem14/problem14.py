import datetime

memory = dict()


def count_colatz(number: int) -> int:
    """
    Count the number of terms of the colatz sequence starting at a given n
    :param number: starting n
    :return: number of terms of the colatz sequence
    """

    count = 1
    n = number
    while n>1:

        if n in memory:
            count += memory[n]-1
            break

        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1
        count += 1

    memory[number] = count
    return count


def count_colatz_recursive(number: int) -> int:
    """
    Count the numbers in the colatz sequence through a recursive approach
    :param number: given integer
    :return: number of terms of the colatz sequence for the given number
    """

    if number == 1:
        return 1

    if number in memory:
        return memory[number]

    if number%2 == 0:
        count = count_colatz_recursive(number//2) + 1
    else:
        count = count_colatz_recursive(3*number+1) + 1

    memory[number] = count

    return count

start_time = datetime.datetime.now()
longest_chain = 0
longest_number = 0
for n in range(1000000):
    count = count_colatz(n)
    if count>longest_chain:
        longest_chain = count
        longest_number = n

print(longest_number)
print(datetime.datetime.now()-start_time)

start_time = datetime.datetime.now()
longest_chain = 0
longest_number = 0
for n in range(1000000):
    count = count_colatz_recursive(n)
    if count>longest_chain:
        longest_chain = count
        longest_number = n

print(longest_number)
print(datetime.datetime.now()-start_time)
