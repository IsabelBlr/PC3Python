def obtener_calificaciones():
    while True:
        calificaciones_input = input("Ingrese las calificaciones separadas por comas: ")
        calificaciones_lista = calificaciones_input.split(',')
        try:
            calificaciones_enteros = [int(calificacion.strip()) for calificacion in calificaciones_lista]
            return calificaciones_enteros
        except ValueError:
            print("Error: Al menos una de las calificaciones no es un número entero. Por favor, inténtelo de nuevo.")

if __name__ == "__main__":
    try:
        calificaciones = obtener_calificaciones()
        print("Calificaciones ingresadas:", calificaciones)
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")