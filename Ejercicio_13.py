#Diseña un pequeño juego de aventura basado
# en texto. El jugador comienza en una habitación
# y puede tomar decisiones ('ir al norte', 'abrir cofre'):
#El juego debe tener al menos 3 habitaciones
# y un estado final (ganar o perder).
def mostrar_instrucciones():
    """
    Muestra las instrucciones básicas del juego.
    """
    print("""
    🏰 Bienvenido a la Aventura de Texto 🏰
    Estás atrapado en un castillo misterioso. 
    Tu objetivo es encontrar la salida sin caer en trampas.

    Comandos disponibles:
    - 'norte'
    - 'sur'
    - 'este'
    - 'oeste'
    - 'abrir cofre'
    - 'salir'
    """)


def validar_entrada(accion: str) -> str:
    """Valida lo que el jugador hace en la habitación 'entrada'."""
    if accion == "norte":
        return "biblioteca"
    elif accion == "este":
        return "sotano"
    elif accion == "salir":
        return "salir"
    else:
        return "Opción inválida. Intenta de nuevo."


def validar_biblioteca(accion: str) -> str:
    """Valida lo que el jugador hace en la 'biblioteca'."""
    if accion == "abrir cofre":
        return "ganaste"
    elif accion == "sur":
        return "entrada"
    else:
        return "Opción inválida. Intenta de nuevo."


def validar_sotano(accion: str) -> str:
    """Valida lo que el jugador hace en el 'sotano'."""
    if accion == "oeste":
        return "entrada"
    else:
        return "perdiste"


def aventura():
    """
    Juego principal que usa las funciones de validación.
    """
    habitacion_actual = "entrada"
    juego_activo = True

    while juego_activo:
        print(f"\nTe encuentras en la habitación: {habitacion_actual}")

        if habitacion_actual == "entrada":
            print("Ves dos puertas: una al norte y otra al este.")
            accion = input("¿Qué deseas hacer?: ").strip().lower()
            resultado = validar_entrada(accion)



            if resultado in ["biblioteca", "sotano", "entrada"]:
                habitacion_actual = resultado
            elif resultado == "salir":
                print("Has decidido abandonar el castillo.")
                juego_activo = False
            else:
                print(resultado)

        elif habitacion_actual == "biblioteca":
            print("Estás en una antigua biblioteca. Hay un cofre misterioso aquí.")
            accion = input("¿Qué deseas hacer? abrir cofre/sur: ").strip().lower()
            resultado = validar_biblioteca(accion)

            if resultado == "ganaste":
                print("¡Encontraste la llave mágica de la salida! Ganaste!!!!")
                juego_activo = False
            elif resultado == "entrada":
                habitacion_actual = "entrada"
            else:
                print(resultado)

        elif habitacion_actual == "sotano":
            print("Has entrado en un sótano oscuro... ¡un monstruo aparece! ")
            accion = input("¿Qué deseas hacer? salir/oeste: ").strip().lower()
            resultado = validar_sotano(accion)

            if resultado == "entrada":
                habitacion_actual = "entrada"
            else:
                print("El monstruo te atrapó... ¡Perdiste!")
                juego_activo = False


def main():
    mostrar_instrucciones()
    aventura()


if __name__ == "__main__":
    main()
