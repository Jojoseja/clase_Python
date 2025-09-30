while True:
    try:
        clave = (input("Ingrese la clave: "))
        if clave=="python123":
            print("Acceso Concedido")
            break
        else:
            raise Exception
    except:
        print("Ingrese la clave correcta")
        del clave
