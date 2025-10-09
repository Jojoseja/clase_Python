class Alumno:
    contador = 1

    def __init__(self, nombre, apellidos, py, dm, ds, calc, oop, java, cplus, db, webdev, ai):
        self.id = Alumno.contador
        self.nombre = nombre
        self.apellidos = apellidos
        self.py = py
        self.dm = dm
        self.ds = ds
        self.calc = calc
        self.oop = oop
        self.java = java
        self.cplus = cplus
        self.db = db
        self.webdev = webdev
        self.ai = ai
        Alumno.contador += 1

    def to_dict(self):
        return {"ID": self.id, "Nombre": self.nombre, "Apellidos": self.apellidos, "Python": self.py,
                "Discrete Mathematics": self.dm, "Data Structures": self.ds, "Calculus": self.calc,
                "Object-Oriented Programming": self.oop, "Java": self.java, "C++": self.cplus, "Databases": self.db,
                "Web Development": self.webdev, "AI": self.ai
                }
