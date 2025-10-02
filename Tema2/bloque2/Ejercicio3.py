import math

try:
    print("Programa para solucionar ecuaciones cuadraticas")
    numa = float(input("Introduce el coeficiente A: "))
    if numa == 0:
        raise ValueError("El coeficiente A no puede ser negativo")
    numb = float(input("Introduce el coeficiente B: "))
    numc = float(input("Introduce el coeficiente C: "))

    discriminante = pow(numb, 2) - 4 * numa * numc
    if discriminante < 0:
        print("No tiene soluciones positivas")
        raise ValueError("No tiene discriminante positivo")
    elif discriminante == 0:
        try:
            raiz = (-numb + math.sqrt(discriminante)) / (2 * numa)
        except:
            raiz = (-numb - math.sqrt(discriminante)) / (2 * numa)
        finally:
            print(f"El valor de la raiz es: {raiz}")
    else:
        raiz1 = (-numb + math.sqrt(discriminante)) / (2 * numa)
        raiz2 = (-numb - math.sqrt(discriminante)) / (2 * numa)
        print(f"El valor de la raiz1 es: {raiz1} y de la raiz2 es: {raiz2}")
except:
    print("Error")