# Find the sum of all multiples of 3 or 5 up to below 1000



def sumOfMultiples():
    # total sum of all multiples
    total_sum = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i

    return total_sum


print(sumOfMultiples())