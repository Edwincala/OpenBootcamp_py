class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def print_attr(self):
        return f"Estudiante: {self.nombre} \tNota:  {self.nota}"

    def aprueba(self):
        if self.nota >= 7.0:
            return "Aprueba"
        else:
            return "No aprueba"


alumno1 = Alumno("ABC", 8.5)

print(alumno1.print_attr() + "\t" + alumno1.aprueba())

alumno2 = Alumno("DEF", 5.3)

print(alumno2.print_attr() + "\t" + alumno2.aprueba())
