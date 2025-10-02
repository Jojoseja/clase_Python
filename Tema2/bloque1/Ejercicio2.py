# Solicitar dos números y mostrar cual es mayor, cual es menor o si son iguales

try:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    if num1 > num2:
        print(f"El número {num1} es mayor que {num2}")
    if num1 < num2:
        print(f"El número {num2} es mayor que {num1}")
    else:
        print(f"Ambos números son iguales")
except:
    print("Ingrese un numero valido")