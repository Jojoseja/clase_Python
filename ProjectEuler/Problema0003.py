# Largest prime factor of the number 600 851 475 143


def primeFactor(n):
    prime_factors = []

    # First Prime
    i = 2
    while n != 1:
        if n % i == 0:
            prime_factors.append(i)
            n = n / i
        else :
            i += 1

    return prime_factors

print(primeFactor(600851475143))
