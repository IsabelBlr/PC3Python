import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio**2

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

def menu():
    print("Menú:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def calcular_area_circulo():
    radio = float(input("Introduce el radio del círculo: "))
    circulo = CIRCULO(radio)
    print("El área del círculo es:", circulo.calcular_area())

def calcular_area_rectangulo():
    largo = float(input("Introduce el largo del rectángulo: "))
    ancho = float(input("Introduce el ancho del rectángulo: "))
    rectangulo = RECTANGULO(largo, ancho)
    print("El área del rectángulo es:", rectangulo.calcular_area())

def calcular_area_cuadrado():
    lado = float(input("Introduce el lado del cuadrado: "))
    area = lado ** 2
    print("El área del cuadrado es:", area)

while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        calcular_area_circulo()
    elif opcion == "2":
        calcular_area_rectangulo()
    elif opcion == "3":
        calcular_area_cuadrado()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")