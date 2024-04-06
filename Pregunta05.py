class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        else:
            print("Edad: No definida")
        if self.notas:
            print("Notas:", self.notas)
        else:
            print("Notas: No definidas")

    def set_age(self, edad):
        self.edad = edad

    def set_notas(self, *notas):
        self.notas = notas

if __name__ == "__main__":
    try:
        nombre = input("Ingrese el nombre del alumno: ")
        numero_registro = input("Ingrese el número de registro del alumno: ")
        alumno = Alumno(nombre, numero_registro)
        alumno.display()
        edad = int(input("Ingrese la edad del alumno: "))
        alumno.set_age(edad)
        notas_input = input("Ingrese las notas del alumno separadas por espacios: ")
        notas = [float(nota) for nota in notas_input.split()]
        alumno.set_notas(*notas)
        alumno.display()
    except ValueError:
        print("Error: La edad debe ser un número entero y las notas deben ser números reales.")