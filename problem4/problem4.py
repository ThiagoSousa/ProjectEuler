import datetime


def is_palindromic(n: int) -> bool:
    """
    Check if a number is palindromic
    :param n: an integer
    :return: True or False on whether it is palindromic or not.
    """

    return str(n) == str(n)[::-1]

start_time = datetime.datetime.now()
largest_palindromic = 0
products = []
for i in range(100, 1000):
    for j in range(i, 1000):
        products.append(i * j)

products = sorted(products, reverse=True)
for product in products:
    if is_palindromic(product):
        print(product)
        break
print(f"Time {datetime.datetime.now()-start_time}")

