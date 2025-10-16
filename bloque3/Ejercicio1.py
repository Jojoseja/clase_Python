# cantidad a invertir
# interes anual
# numero de años

def recibirDatos():
    while True:
        try:
            invertir = float(input("Ingrese el dinero a invertir: "))
            if invertir < 0:
                raise Exception
            interes = float(input("Ingrese un numero %: "))
            if interes < 0:
                raise Exception
            years = int(input("Ingrese el numero de años: "))
            if years < 0:
                raise Exception
            break
        except ValueError:
            print("El valor ingresado no es un numero válido")
    return [invertir, interes, years]

lista = recibirDatos()

for i in range(lista[2]+1):
    if i == 0:
        print(f"Dinero inicial: {lista[0]}")
    else:
        print(f"Dinero el año {i}: {lista[0]:.2f}")
    lista[0] *= (lista[1]/100) + 1