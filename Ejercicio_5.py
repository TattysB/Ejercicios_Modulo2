#Crea un programa que pida un número y, usando
# un operador ternario, asigne a una variable el texto
# "Par" o "Impar". Luego, imprime el resultado.
# Adicionalmente, si el número es múltiplo de 5,
# debe imprimir un mensaje extra.


def clasificar_numero(numero: int) -> str:
    """
    Clasifica un número si es impar o par y revisa
    si es múltiplo de 5.

    Args:
        numero (int): Número ingresado por el usuario.

    Returns:
        str: Mensaje con la clasificación del número.
    """
    resultado = "Par" if numero % 2 == 0 else "Impar"

    if numero % 5 == 0:
        resultado += " y múltiplo de 5"

    return resultado


def validar_numero(num: str) -> int:
    """
    Valida que el número ingresado sea correcto.

    Args:
        num (str): Entrada del usuario.

    Returns:
        int: El número convertido a entero si es válido.

    Raises:
        ValueError: Si la entrada no cumple con las condiciones.
    """
    if num is None or str(num).strip() == "":
        raise ValueError("El campo no puede estar vacío.")


    if not num.lstrip("-").isdigit():
        raise ValueError("Debe ingresar un número entero.")

    numero = int(num)

    if numero < -1000 or numero > 1000:
        raise ValueError("Error. El número tiene que estar dentro de -1000 y 1000.")

    return numero


def main():

    print("--- Clasifica los números Par o Impar ---")

    while True:
        num = input("Ingrese un número entero (o 'q' para salir): ").strip()

        if num.lower() == "q":
            print("Saliendo del programa...")
            break

        try:
            numero = validar_numero(num)  # ✅ Validación con excepción
            resultado = clasificar_numero(numero)
            print(f"Resultado: El número {numero} es {resultado}\n")

        except ValueError as e:
            print(e)  #


if __name__ == "__main__":
    main()
