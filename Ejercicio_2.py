#Desarrolla un programa que simule un menú de
# consola usando la estructura match-case.
# El programa mostrará una lista de comandos
# disponibles ("guardar", "cargar", "salir")
# y el usuario ingresará uno

def ejecutar_comando(comando):
    """
    Ejecuta la acción según el comando ingresado.
    Se aceptan tanto palabras como números.
    """
    match comando:
        case "1" | "guardar":
            print("Guardando el archivo...")
        case "2" | "cargar":
            print("Cargando el archivo...")
        case "3" | "imprimir":
            print("Imprimiendo el archivo...")
        case "4" | "salir":
            print("Saliendo del programa...")
        case _:
            print(" Error: comando no reconocido. Intente nuevamente.")


def pedir_comando(comando):
    """
    Pide al usuario un comando y valida que:
    - No esté vacío
    - Sea número válido del menú o letras sin símbolos
    Retorna el comando en minúsculas o como número.
    """
    while True:

        if comando is None or str(comando).strip() == "":
            raise ValueError("El campo no puede estar vacío.")
            continue

        if comando.isdigit():
            if comando in ["1", "2", "3", "4"]:
                return comando
            else:
                return 'Error: número fuera de rango.'
                continue

        if not comando.isalpha():  # Si escribió algo que no son solo letras
            return " Error: Solo se aceptan letras o números válidos del menú."
            continue

        return comando  # Si esta bien lo retorna


def mostrar_menu():
    """
    Muestra los comandos disponibles al usuario.
    """
    print("\n--- Menú de comandos ---")
    print("1 - guardar")
    print("2 - cargar")
    print("3 - imprimir")
    print("4 - salir")

def main():

    print("\n=== Bienvenido al programa ===")

    while True:
        mostrar_menu()
        entrada = input("\nEscriba un comando (número o palabra): ").strip().lower()
        comando = pedir_comando(entrada)
        ejecutar_comando(comando)

        if comando in ["4", "salir"]:
            break

if __name__ == "__main__":
    main()
