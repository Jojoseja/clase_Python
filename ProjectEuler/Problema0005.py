# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

# Chapuza

# comprobar numeros primos
def checkPrime(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    return prime

# returns dictionary with divisors
def decompose(number):
    if checkPrime(number):
        divisor = {number:1}
    else:
        primeList = []
        for i in range(2, number):
            if checkPrime(i):
                primeList.append(i)

        divisor = {}

        for p in primeList:
            divisor[p] = 0

        i = 2
        while number != 1 and i <= number:
            if number % i == 0:
                divisor[i] += 1
                number /= i
            else:
                i += 1

    return divisor

# @number: maximo numero divisible
def smallestPositiveNumber(number):

    primeList = []
    for i in range(2, number+1):
        if checkPrime(i):
            primeList.append(i)

    primeDict = {}

    for p in primeList:
        primeDict[p] = 0

    for i in range(2, number+1):
        newDict = decompose(i)
        for p in newDict:
            if newDict[p] >= primeDict[p]:
                primeDict[p] = newDict[p]



    total_sum = 1
    for p in primeDict:
        total_sum *= pow(p, primeDict[p])

    return total_sum

print(f"{smallestPositiveNumber(50):,}")