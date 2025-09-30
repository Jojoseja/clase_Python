while True:
    try:
        print("Seleccion 1. Ver perfil  2. Editar Perfil  3. Salir")
        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            print("Viendo Perfil")
        if opcion == 2:
            print("Editar Perfil")
        if opcion == 3:
            print("Salir")
            break
    except:
        print("Ingrese una opción válida")