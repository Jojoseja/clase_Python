import math

problema_resuelto = False

a, b, c = 0,0,0

while not problema_resuelto:
    a += 1
    if (a + b + c) == 1000 and pow(a, 2) + pow(b, 2) == pow(c, 2):
        problema_resuelto = True
    elif a == 500:
        a = 0
        b += 1

    elif b == 600:
        a = 0
        b = 0
        c += 1



# 200, 375, 425
print(a, b, c)