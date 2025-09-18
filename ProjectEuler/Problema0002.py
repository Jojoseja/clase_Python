# Sum of all even Fibonacci numbers up to 4 000 000

def evenFibo():
    # sum of even fibo numbers
    total_sum = 0

    # a = 0, b = 1
    a, b = 0, 1

    while b < 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            total_sum += b

    return total_sum

print(evenFibo())