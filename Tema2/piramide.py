try:
    num = int(input("Ingrese un numero: "))
except:
    print("El numero es invalido")

for i in range(0, num):
    cadena = "*" * 2 * i + "*"
    cadena = cadena.center(2*num)
    print(cadena)