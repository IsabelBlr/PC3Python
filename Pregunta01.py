def obtener_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y (donde X e Y son enteros y X <= Y, Y != 0): ")
            numerador, denominador = map(int, fraccion.split('/'))
            if denominador == 0 or numerador > denominador:
                raise ValueError
            return numerador, denominador
        except ValueError:
            print("Error: Ingrese una fracción válida en el formato especificado.")

def calcular_porcentaje(numerador, denominador):
    try:
        porcentaje = (numerador / denominador) * 100
        porcentaje_redondeado = round(porcentaje)
        if porcentaje_redondeado <= 1:
            return 'E'
        elif porcentaje_redondeado >= 99:
            return 'F'
        else:
            return f'{porcentaje_redondeado}%'
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

if __name__ == "__main__":
    while True:
        numerador, denominador = obtener_fraccion()
        resultado = calcular_porcentaje(numerador, denominador)
        if resultado:
            print("Cantidad de combustible en el tanque:", resultado)
            break