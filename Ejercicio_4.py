#Implementa el clásico juego para jugar
# contra la computadora piedra papel o tijera

import random

opciones = ["piedra", "papel", "tijera"]


def validar_eleccion(usuario, opcion):
    """
    Validda que la elección que ingresa el usuario sea
    válida.

    Args:
        usuario (string): usuario que ingresa el usuario
        computador (list) :Lista de opciones

    Returns:
        bool: True si la opción es válida o
        False si es lo contrario

    """

    return usuario in opciones  # Lo devuelve si la opción del usuario esta dentro de la lista


def jugar_ronda(usuario, computador):
    """
    Determina quien es el ganador de cada ronda
    """

    if usuario is None or str(usuario).strip() == "":
        return "El campo no puede estar vacío."

    usuario = usuario.strip().lower()

    if not validar_eleccion(usuario, opciones):
        return "Error. Opción invalida, intente nuevo."

    if usuario == computador:
        return "Empate"
    elif (usuario == "piedra" and computador == "tijera") or \
            (usuario == "papel" and computador == "piedra") or \
            (usuario == "tijera" and computador == "papel"):
        return "usuario"
    else:
        return "computador"

def main():

    victoria_usuario = 0
    victoria_computador = 0

    print("---Juego PIEDRA,PAPEL o TIJERA---")
    print("El primero en ganar las tres veces se lleva la Victoria!!!!")



    while victoria_usuario < 3 and victoria_computador < 3:  #se repite hasta que alguien llegue a 3 victorias
        usuario = input("Elija la opción Piedra, Papel o Tijera:  ").lower().strip()

        if not validar_eleccion(usuario, opciones):  # Valida si lo que escribió el usuario es válido
            print("Error. Opción invalida, intente nuevo.")
            continue

        computador = random.choice(opciones)
        print(f"El computador eligio: {computador}")

        resultado = jugar_ronda(usuario, computador)

        if resultado == "empate":
            print("¡¡ Empate !!...")
        elif resultado == "usuario":
            victoria_usuario += 1
            print("¡Felicitaciones!!Ganaste esta ronda...")
        else:
            victoria_computador += 1
            print("Perdiste esta ronda...")

        print(f"Marcador -> Tu: {victoria_usuario} | Computadora: {victoria_computador} \n")

    if victoria_usuario == 3:
        print("Felicitaciones!! Ganaste la partida..")
    else:
        print("La computadora gano.¡Ten mas suerte para la próxima!!!")


if __name__ == "__main__":
    main()
