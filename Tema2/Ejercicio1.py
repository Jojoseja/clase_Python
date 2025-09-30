# validar la edad -> mayor de 0 y numero entero

try :
    edad = int(input("Ingrese su edad: "))
    if edad < 1:
        raise Exception("La edad no debe ser menor que 1")
    if edad >= 18:
        print("El usuario es mayor de edad")
    else:
        print("El usuario es menor de edad")
except :
    print("Ingrese un numero valido")


