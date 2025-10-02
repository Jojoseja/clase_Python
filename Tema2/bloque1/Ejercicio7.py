try:
    num = int(input("Ingrese un numero: "))
    if num >= 0 and num < 14:
        print("No puede conducir")
    elif num >= 14 and num < 16:
        print("Moto de poca cilindrada")
    elif num >= 16 and num < 18:
        print("Moto de gran cilindrada")
    elif num >= 18:
        print("Coche")
    else:
        raise Exception("Error")
except:
    print("Error")