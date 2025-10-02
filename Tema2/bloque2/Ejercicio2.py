try:
    dinero = float(input("Introduce el dinero a convertir: "))
    if dinero < 0:
        raise ValueError("Dinero no puede ser negativo")
    print("Selecciona la divisa: 1.USD, 2.GBP o 3.JPY")
    opcion = int(input())
    if opcion != 1 and opcion != 2 and opcion != 3:
        raise ValueError("Opcion no puede no ser una opcion valida")
    eur_to_dollar = 1.17
    eur_to_gbp = 0.87
    eur_to_jpy = 172,81

    if opcion == 1:
        print(f"La cantidad {dinero} equivale a {dinero*eur_to_dollar} USD")

    if opcion == 2:
        print(f"La cantidad {dinero} equivale a {dinero * eur_to_gbp} GBP")

    if opcion == 3:
        print(f"La cantidad {dinero} equivale a {dinero * eur_to_jpy} JPY")

except:
    print("El numero es incorrecto")