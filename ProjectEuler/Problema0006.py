# Diferecia de Cuadrado de la suma y suma de Cuadrados

def sumaCuadrados(numero):
    total = 0
    for i in range(1, numero+1):
        total += i ** 2

    return total

def cuadradosSuma(numero):
    total = 0
    for i in range(1, numero+1):
        total += i

    return total ** 2


numero = 100

print(cuadradosSuma(numero) - sumaCuadrados(numero))