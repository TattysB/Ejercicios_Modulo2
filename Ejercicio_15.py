#Crea una versión del juego "Batalla Naval"
# en una cuadrícula de 5x5
import random   # Importamos random para colocar el barco en una posición aleatoria




def crear_tablero():
    """
    Crea un tablero vacío de 5x5 representado con listas anidadas.
    Cada celda comienza con '~' (agua sin disparar).
    """
    return [["~" for _ in range(5)] for _ in range(5)]


def imprimir_tablero(tablero):
    """
    Muestra el tablero en pantalla con letras (A-E) para filas
    y números (1-5) para columnas.
    """
    print("  1 2 3 4 5")  # Encabezado de columnas
    letras = "ABCDE"
    for i, fila in enumerate(tablero):
        # Ejemplo de salida:
        # A ~ ~ ~ ~ ~
        print(letras[i], " ".join(fila))


def colocar_barco():
    """
    Coloca un barco de 3 casillas en el tablero, ya sea en fila (H) o columna (V).
    Devuelve una lista de coordenadas [(fila, col), ...] que representan el barco.
    """
    orientacion = random.choice(["H", "V"])  # Elige orientación aleatoria
    barco = []

    if orientacion == "H":  # Barco horizontal
        fila = random.randint(0, 4)       # Escoge una fila (0-4)
        col_inicio = random.randint(0, 2) # Escoge columna de inicio (máx. 2 para que quepan 3 casillas)
        barco = [(fila, col_inicio + i) for i in range(3)]
    else:  # Barco vertical
        fila_inicio = random.randint(0, 2) # Escoge fila inicial (máx. 2 para que quepan 3 casillas hacia abajo)
        col = random.randint(0, 4)         # Escoge columna
        barco = [(fila_inicio + i, col) for i in range(3)]

    return barco


def convertir_coordenada(coordenada):
    """
    Convierte la coordenada ingresada (ej. 'A3') en índices (fila, columna).
    Devuelve una tupla (fila, col) o None si es inválida.
    """
    letras = "ABCDE"
    if len(coordenada) != 2:  # Validamos que la coordenada tenga 2 caracteres
        return None

    fila = coordenada[0].upper()  # Letra en mayúscula (ej. 'a' -> 'A')
    col = coordenada[1]           # El número (string)

    # Validamos letra y número
    if fila not in letras or not col.isdigit():
        return None

    fila_idx = letras.index(fila)  # Convertimos letra en índice (A=0, B=1, etc.)
    col_idx = int(col) - 1         # Convertimos número en índice (1=0, 2=1, etc.)

    # Verificamos que esté dentro del tablero
    if 0 <= fila_idx < 5 and 0 <= col_idx < 5:
        return fila_idx, col_idx
    return None



def validar_coordenada(coordenada):
    """
    Valida si la coordenada es correcta (ej. 'A3' dentro del tablero).
    Retorna True si es válida, False si no.
    """
    return convertir_coordenada(coordenada) is not None


def validar_disparo_repetido(coordenada, disparos_realizados):
    """
    Verifica si ya se disparó en esa coordenada.
    Retorna True si ya se usó, False si es nueva.
    """
    return coordenada in disparos_realizados




def main():
    tablero = crear_tablero()        # Tablero vacío
    barco = colocar_barco()          # Colocamos el barco (oculto al jugador)
    vidas = 10                       # Intentos disponibles
    aciertos = 0                     # Contador de impactos al barco
    disparos_realizados = set()      # Guardamos los disparos para no repetir

    print("¡Bienvenido a Batalla Naval! 🚢")
    imprimir_tablero(tablero)        # Mostramos tablero inicial

    # Bucle principal del juego
    while vidas > 0 and aciertos < 3:
        disparo = input("Ingresa coordenada (ej. A3): ").strip()

        # 🔎 Usamos validaciones externas
        if not validar_coordenada(disparo):
            print("Entrada inválida. Usa formato como A3.")
            continue

        coordenada = convertir_coordenada(disparo)

        if validar_disparo_repetido(coordenada, disparos_realizados):
            print("Ya disparaste en esa coordenada. Intenta otra.")
            continue

        # Guardamos el disparo como usado
        disparos_realizados.add(coordenada)
        fila, col = coordenada

        if coordenada in barco:  # Impacto
            print("¡Tocado! 🔥")
            tablero[fila][col] = "X"
            aciertos += 1
        else:  # Agua
            print("Agua 🌊")
            tablero[fila][col] = "O"

        vidas -= 1
        imprimir_tablero(tablero)
        print(f"Te quedan {vidas} vidas.\n")

    # Fin del juego
    if aciertos == 3:
        print("¡Felicidades! Hundiste el barco 🚢💥")
    else:
        print("Te quedaste sin vidas. Perdiste 😢")
        print("El barco estaba en:", barco)



if __name__ == "__main__":
    main()
