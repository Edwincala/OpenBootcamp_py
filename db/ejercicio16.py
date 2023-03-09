import sqlite3



def crear_alumno(id, nombre, apellido):
    conn = sqlite3.connect('./Alumnos.db')

    cursor = conn.cursor()

    query = '''INSERT INTO Alumnos (id, nombre, apellido) values(?, ?, ?)'''

    cursor.execute(query, (id, nombre, apellido))
    conn.commit()

    print(f"Registro con id {cursor.lastrowid} ingresado exitosamente")

    cursor.close()

    conn.close()

    
# crear_alumno(1, 'Juan', 'Perez')
# crear_alumno(2, 'Valentina', 'Laverde')
# crear_alumno(3, 'Sara', 'Sánchez')
# crear_alumno(4, 'Efraín', 'Casas')
# crear_alumno(5, 'Julieta', 'Ponce')
# crear_alumno(6, 'Martín', 'Ríos')
# crear_alumno(7, 'Carlos', 'García')
# crear_alumno(8, 'Bernardo', 'López')


def mostrar_alumno(nombre):
    conn = sqlite3.connect('./Alumnos.db')

    cursor = conn.cursor()

    query = '''SELECT * FROM Alumnos WHERE nombre=?'''

    cursor.execute(query, (nombre,))
    alumno = cursor.fetchone()

    print(f"Id: {alumno[0]} | Nombre: {alumno[1]} | Apellido: {alumno[2]}")

    cursor.close()

    conn.close()


mostrar_alumno('Sara')


