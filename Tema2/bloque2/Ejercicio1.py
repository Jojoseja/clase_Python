import math
def primoCheck(num):
    if num == 2 or num == 3:
        print("Es un primo")
        return True
    if num % 2 == 0:
        print("Es divisible entre 2")
        return False
    if num % 3 == 0:
        print("Es divisible entre 3")
        return False

    for i in range(6, math.floor(math.sqrt(num))+2, 6):
        if num % (i - 1) == 0:
            num2 = i - 1
            print(f"Es divisible entre: {num2}")
            return False
        elif num % (i + 1) == 0:
            num2 = i + 1
            print(f"Es divisible entre: {num2}")
            return False

    print("Es primo")
    return True

try :
    num = int(input())
    if num < 2:
        raise ValueError("Numero invalido")
    print(primoCheck(num))
except :
    print("El numero es invalido")

