# Nota numerica entre 0 y 10 incluyendo decimales

try:
    num1 = float(input("Ingrese la nota: "))

    if num1 >= 0 and num1 < 5:
        print("Suspenso")
    if num1 >= 5 and num1 < 7:
        print("Aprobado")
    if num1 >= 7 and num1 < 9:
        print("Notable")
    if num1 >= 9 and num1 <= 10:
        print("Sobresaliente")
    else:
        raise Exception("El numero no es valido")
except:
    print("Ingrese un numero valido")