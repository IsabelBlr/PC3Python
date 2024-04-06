class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

if __name__ == "__main__":
    try:
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        mi_rectangulo = Rectangulo(largo, ancho)
        area = mi_rectangulo.calcular_area()
        print("El área del rectángulo es:", area)
    except ValueError:
        print("Error: El largo y el ancho deben ser números reales.")