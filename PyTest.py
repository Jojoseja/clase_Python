class Ejemplo():
    def __init__(self, nombre="Carlos", edad=7, modifier="algo"):
        self.nombre = nombre
        self.edad = edad
        self.modifier = modifier



a = Ejemplo(modifier="hola",edad=11)

print(a.nombre)
print(f"{a.nombre}, {a.edad}, {a.modifier}")