# Numero primo 10001
# comprobar numeros primos
import math

def checkPrime(number):
    prime = True
    for i in range(2, number//2):
        if number == 4:
            return False
        if number % i == 0:
            prime = False
    return prime

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for x in range(6, math.floor(math.sqrt(n)) + 2, 6):
        if n % (x - 1) == 0 or n % (x + 1) == 0:
            return False
    return True

list = []

counter = 0

i = 1

#104743
while counter != 10001:
    i += 1
    if is_prime(i):
        counter += 1


print(i)