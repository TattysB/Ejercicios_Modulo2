#Crea una función que reciba una matriz
# (lista de listas) y devuelva su transpuesta.
# La transpuesta se logra intercambiando filas por columnas.


def mover_matriz(matriz):
    """
    Recibe una matriz (una lista de unas listas)
    y devuelve su transpuesta.La transpuesta se logra
    intercambiando filas por columnas.

    """

    filas = len(matriz)
    columnas = len(matriz[0])

    transpuesta = []

    for j in range(columnas):  # Recorremos las columnas de la matriz
        nueva_fila = []
        for i in range(filas):
            nueva_fila.append(matriz[i][j])  # se toma el elemento [i][j] y lo guardamos
        transpuesta.append(nueva_fila)  # añadimos la fila construida a la transpuesta

    return transpuesta
def main():

    matriz= [[2,4,6],[3,5,7],[8,9,0]]
    print(f"Matriz original: {matriz}")
    print(f"Matriz transpuesta: {mover_matriz(matriz)}")


if __name__ == "__main__":
    main()