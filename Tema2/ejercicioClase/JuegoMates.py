import random as rand


def randomSuma():
    num1 = rand.randint(1,10)
    num2 = rand.randint(1,10)
    num3 = num1 + num2
    return num1,num2,num3


while (True):
    try:
        lista = randomSuma()
        res = int(input(f"La suma de {lista[0]} + {lista[1]} = ? "))
        if res==lista[2]:
            print(f"Respuesta correcta !")
            break
    except ValueError:
        print("Ingresa un número válido")