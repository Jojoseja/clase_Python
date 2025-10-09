numeros = []

while len(numeros) != 5:
    try:
        numeros.append(int(input("Ingrese un numero: ")))
    except:
        print("El numero ingresado no es valido")

numeros.sort()

print(numeros)