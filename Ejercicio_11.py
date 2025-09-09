#Escribe una función que valide un número de cédula
# (como string) basado en una regla simple:
# la suma de sus dígitos debe ser un número par.
# La función debe devolver True si es válido y False si no:
#Adicionalmente, el programa principal debe pedir
# al usuario su cédula hasta que ingrese una
# válida, usando un bucle.

def validar_cedula(cedula: str) -> bool:
    """
    Valida que la suma de los dígitos de la cédula sea par.

    Args:
        cedula (str): Número de cédula.

    Returns:
        bool: True si la suma es par, False en caso contrario.
    """
    suma = 0
    for digito in cedula:
        suma += int(digito)
    return suma % 2 == 0


def validar_vacio(cedula: str) -> str:
    """
    Valida que el campo no esté vacío.

    """
    if cedula is None or str(cedula).strip() == "":
        raise ValueError("El campo no puede estar vacío.")
    return cedula


def validar_numerico(cedula: str) -> str:
    """
    Valida que solo contenga números.

    """
    if not cedula.isdigit():
        raise ValueError("Error. La cédula solo puede contener números.")
    return cedula


def validar_longitud(cedula: str) -> str:
    """
    Valida que tenga entre 10 y 11 dígitos.

    """
    if len(cedula) < 10 or len(cedula) > 11:
        raise ValueError("Error. El número de cédula tiene que tener entre 10 y 11 dígitos.")
    return cedula


def main():
    while True:
        try:
            cedula = input("Ingrese el número de su cédula: ").strip()

            # Validaciones en cadena
            cedula = validar_vacio(cedula)
            cedula = validar_numerico(cedula)
            cedula = validar_longitud(cedula)

            if validar_cedula(cedula):
                print("Número de cédula válido. ¡Bienvenid@!..")
                break
            else:
                print("Número de cédula inválida. Intente de nuevo.")

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
