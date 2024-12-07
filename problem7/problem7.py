from utils.prime_functions import next_prime
import datetime

start_date = datetime.datetime.now()
prime = 2
i = 1
while i < 10001:
    prime = next_prime(prime)
    i += 1
print(prime)
print(f"Time: {datetime.datetime.now()-start_date}")
