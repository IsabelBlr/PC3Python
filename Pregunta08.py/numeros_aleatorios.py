import random

def generar_numeros_aleatorios():
    return [random.randint(0, 100) for _ in range(20)]

def mostrar_lista(lista):
    print("Lista de números aleatorios:")
    print(lista)

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    print(lista_ordenada)