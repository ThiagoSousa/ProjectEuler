from utils.prime_functions import next_prime
from utils.prime_functions import sieve_of_eratosthenes
import datetime

# complexity: O(sqrt(n)*n)
start_time = datetime.datetime.now()
prime = 2
limit = 2000000
s = 0
while prime < limit:
    s += prime
    prime = next_prime(prime)
print(s)
print(f"Time Individual Check: {datetime.datetime.now()-start_time}")

# complexity: O(n*loglogn)
start_time = datetime.datetime.now()
limit = 2000000
primes = sieve_of_eratosthenes(limit=limit)
print(sum(primes))
print(f"Time Sieve: {datetime.datetime.now()-start_time}")
