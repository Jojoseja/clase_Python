# Find the sum of all primes below 2 000 000
import math as math

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for x in range(6, math.floor(math.sqrt(n)) + 2, 6):
        if n % (x - 1) == 0 or n % 1(x + 1) == 0:
            return False
    return True


total_sum = 0
max_range = 2000000

for i in range(max_range):
    if is_prime(i):
        total_sum += i

print(f"The sum of all primes below {max_range} is {total_sum}")