import datetime
from utils.prime_functions import next_prime

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
