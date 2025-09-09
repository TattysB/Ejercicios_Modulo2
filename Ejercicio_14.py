# Diseña una versión para consola del clásico
# juego del "Ahorcado". El programa debe ser capaz
# de gestionar toda la lógica del juego, desde
# la selección de la palabra hasta determinar
# si el jugador ha ganado o perdido.
import random  # para elegir una palabra al azar desde una lista
import string  # para acceder a clases de caracteres (ascii_lowercase)


def seleccionar_palabra(palabras):
    """
    Selecciona aleatoriamente una palabra de la lista dada.
    """
    return random.choice(palabras).lower()


def mostrar_tablero(palabra_secreta, letras_acertadas, letras_fallidas, vidas):
    """
    Muestra en pantalla el tablero actual del juego: dibujo,
    palabra con guiones y letras intentadas.
    """
    print([vidas])  # Muestra las oportunidades

    # construimos la vista de la palabra: letra si está acertada, '_' si no
    tablero = " ".join([letra if letra in letras_acertadas else "_" for letra in palabra_secreta])
    print("\nPalabra: ", tablero)

    print("Letras acertadas:", " ".join(sorted(letras_acertadas)) if letras_acertadas else "—")
    print("Letras fallidas: ", " ".join(sorted(letras_fallidas)) if letras_fallidas else "—")

    print(f"Vidas restantes: {vidas}\n")


def validar_entrada(entrada, letras_intentadas):
    """
    Valida que la entrada del jugador sea:
      - exactamente 1 carácter,
      - una letra (a-z),
      - no haya sido intentada antes.
    Devuelve (True, letra) si es válida o (False, mensaje_error) si no.
    """
    if entrada == "":
        return False, "Error.No ingresaste nada. Escribe una letra."

    if len(entrada) != 1:
        return False, "Error.Debes ingresar sólo una letra."

    if entrada.lower() not in string.ascii_lowercase:
        return False, "Error.Entrada inválida. Sólo se permiten letras (a-z)."

    letra = entrada.lower()

    if letra in letras_intentadas:
        return False, f"La letra '{letra}' ya fue intentada."

    return True, letra


def juego_ahorcado():
    """
    Ejecuta una partida completa del juego del ahorcado.
    """
    palabras = [
        "python", "programa", "ahorcado", "computadora", "desarrollo",
        "algoritmo", "variable", "funcion", "iteracion", "cadena"
    ]

    palabra = seleccionar_palabra(palabras)
    letras_acertadas = set()
    letras_fallidas = set()
    letras_intentadas = set()
    vidas = 6

    while True:
        mostrar_tablero(palabra, letras_acertadas, letras_fallidas, vidas)

        if all(letra in letras_acertadas for letra in palabra):
            print("¡Felicidades! Has adivinado la palabra:", palabra)
            break

        if vidas == 0:
            print("Te quedaste sin vidas. ¡Has perdido!")
            print("La palabra era:", palabra)
            break

        entrada = input("Ingresa una letra: ").strip()
        valida, resultado = validar_entrada(entrada, letras_intentadas)

        if not valida:
            print("Error:", resultado)
            continue

        letra = resultado
        letras_intentadas.add(letra)

        if letra in palabra:
            letras_acertadas.add(letra)
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
        else:
            letras_fallidas.add(letra)
            vidas -= 1
            print(f"La letra '{letra}' no está en la palabra. Pierdes una vida.")

    # Preguntar si quiere volver a jugar
    while True:
        otra = input("\n¿Quieres jugar otra partida? (s/n): ").strip().lower()
        if otra == "s":
            print("\n--- Nueva partida ---\n")
            return True
        elif otra == "n":
            print("Gracias por jugar. ¡Hasta la próxima!")
            return False
        else:
            print("Por favor responde 's' (sí) o 'n' (no).")


def main():
    """
    Controla la ejecución del juego (una o varias partidas).
    """
    jugar = True
    while jugar:
        jugar = juego_ahorcado()


if __name__ == "__main__":
    main()
