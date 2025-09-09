#Crea un programa que simule el
# lanzamiento de dos dados 10,000 veces.
#Usa un diccionario para contar la frecuencia
# de cada posible suma de los dados (de 2 a 12).
#Al final, imprime un reporte con la frecuencia de cada suma.

import random

def lanzar_dados() -> int:
    """
    Simula el lanzamiento de dos dados y devuelve la suma.
    """
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2


def simular_lanzamientos(n: int) -> dict:
    """
    Simula n lanzamientos de dos dados y devuelve un diccionario
    con la frecuencia de cada suma posible (2 a 12).

    Args:
        n (int): número de lanzamientos

    Returns:
        dict: suma -> frecuencia
    """
    frecuencias = {}
    for _ in range(n):
        suma = lanzar_dados()
        frecuencias[suma] = frecuencias.get(suma, 0) + 1
    return frecuencias


def mostrar_resultados(frecuencias: dict):
    """
    Muestra en consola el resultado de las frecuencias.
    """
    print("Frecuencia de las sumas de los dados:\n")
    for suma in range(2, 13):
        print(f"Suma {suma}: {frecuencias.get(suma, 0)} veces")


def main():
    """
    Función principal que ejecuta la simulación y muestra resultados.
    """
    frecuencias = simular_lanzamientos(10000)
    mostrar_resultados(frecuencias)


if __name__ == "__main__":
    main()

