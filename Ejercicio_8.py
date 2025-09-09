#Ejercicio 8: Filtrado de Datos con List Comprehensions
#Dada una lista de números [-5, 10, -15, 20, -25, 30], utiliza
# una list comprehension para crear tres nuevas listas:
# Una lista con solo los números positivos.
# Una lista con los cuadrados de todos los números.
# Una lista de strings que diga "positivo" o "negativo"
# para cada número, usando un ternario dentro de la comprensión.
# Conceptos aplicados: List comprehensions, operador ternario.


def obtener_positivos(numeros: list) -> list:
    """
    Devuelve solo los números positivos de la lista.

    """
    # Lista con solo los números positivos
    positivos = [n for n in numeros if n > 0]
    return positivos

def obtener_cuadrados(numeros: list) -> list:
    """
    Devuelve los cuadrados de todos los números de la lista.

    """
    # Lista con los cuadrados de todos los números
    cuadrados = [n ** 2 for n in numeros]
    return cuadrados

def obtener_etiquetas(numeros: list) -> list:
    """
    Devuelve 'positivo' o 'negativo' según cada número de la lista.

    """
    # Lista de strings con "positivo" o "negativo"
    etiquetas = ["positivo" if n > 0 else "negativo" for n in numeros]
    return etiquetas

# Función main que llama a las funciones anteriores y muestra resultados
def main():
    numeros = [-5, 10, -15, 20, -25, 30]

    # Llamar a las funciones
    positivos = obtener_positivos(numeros)
    cuadrados = obtener_cuadrados(numeros)
    etiquetas = obtener_etiquetas(numeros)

    # Mostrar resultados
    print("Números originales:", numeros)
    print("Positivos:", positivos)
    print("Cuadrados:", cuadrados)
    print("Etiquetas:", etiquetas)


if __name__ == "__main__":
    main()



