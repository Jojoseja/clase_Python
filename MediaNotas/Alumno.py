class Alumno:
    def __init__(self, nombre, apellidos, mates, biologia, ingles, lengua):
        self.nombre = nombre
        self.apellidos = apellidos
        self.mates = mates
        self.biologia = biologia
        self.ingles = ingles
        self.lengua = lengua

    def to_dict(self):
        return {"Nombre": self.nombre, "Apellidos": self.apellidos, "Mates": self.mates, "Biología": self.biologia,
                "Inglés": self.ingles, "Lengua": self.lengua}
