try:
    num1 = int(input("Ingrese un numero: "))
    if num1 % 2 == 0:
        print("El numero es par")
    if num1 % 2 != 0:
        print("El numero es impar")
    else :
        raise Exception("Error")
except:
    print("Ingrese un numero válido")