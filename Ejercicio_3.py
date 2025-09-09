#Escribe un programa que pida al usuario
# crear una contraseña y la valide usando
# un bucle while.


def validar_contrasena(contrasena: str):
    """
    Valida que la contraseña cumpla con las reglas y
    retorna un mensaje de error o "OK" si es válida.
    """

    if contrasena is None or str(contrasena).strip() == "":
        raise ValueError("El campo no puede estar vacío.")


    if len(contrasena) < 8:  # len() devuelve la cantidad de caracteres
        return "Error: La contraseña debe tener mínimo 8 caracteres."

    if not any(c.isupper() for c in contrasena):  # Verifica que tenga al menos una letra mayúscula
        # any() devuelve True si al menos un carácter cumple la condición
        # c.isupper() revisa si el carácter es mayúscula
        return "Error: La contraseña debe contener al menos una letra MAYÚSCULA."

    if not any(c.isdigit() for c in contrasena):
        # c.isdigit() revisa si el carácter es un dígito (0-9)
        return "Error: La contraseña debe contener al menos un número."

    return "OK"  # Lo retorna si pasa todas las validaciones



def main(value=None):
    print("--- Validar Contraseña ---")

    while True:
        contrasena = input("Crea una contraseña: ").strip()

        resultado = validar_contrasena(contrasena)

        if resultado == "OK":
            print(" Contraseña válida. ¡Registro exitoso!")
            break
        else:
            print(resultado)



if __name__ == "__main__":
    main()
