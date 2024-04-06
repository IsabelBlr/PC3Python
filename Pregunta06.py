class Producto:
    def __init__(self, codigo, nombre, precio, año):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: ${self.precio}, Año: {self.año}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Lista de productos:")
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        print(f"Productos del año {año}:")
        for producto in self.productos:
            if producto.año == año:
                print(producto)


if __name__ == "__main__":
    catalogo = Catalogo()

    # Agregar algunos productos de ejemplo
    catalogo.agregar_producto(Producto("001", "Filtro de aceite", 15.99, 2022))
    catalogo.agregar_producto(Producto("002", "Pastillas de freno", 29.99, 2021))
    catalogo.agregar_producto(Producto("003", "Batería de auto", 99.99, 2023))
    catalogo.agregar_producto(Producto("004", "Llantas", 149.99, 2022))

    # Mostrar todos los productos
    catalogo.mostrar_productos()

    # Filtrar productos por año
    catalogo.filtrar_por_año(2022)