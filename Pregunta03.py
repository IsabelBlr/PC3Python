import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

if __name__ == "__main__":
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        mi_circulo = Circulo(radio)
        area = mi_circulo.calcular_area()
        print("El área del círculo con radio", radio, "es:", area)
    except ValueError:
        print("Error: El radio debe ser un número real.")