#Crea una función que reciba una frase y una letra.
# La función debe devolver una lista con todos los
# índices (posiciones) en los que aparece esa letra
# en la frase.


def encontrar_indices(frase: str, letra: str) -> list:
    """
    Devuelve los índices donde aparece una letra en una frase.

    Args:
        frase (str): Frase en la que se buscará la letra.
        letra (str): Letra que se desea buscar.

    Returns:
        list: Lista de posiciones donde aparece la letra.

    """

    # Búsqueda: recorrer la frase y guardar los índices donde la letra coincide (sin importar mayúsculas/minúsculas)
    posiciones = [i for i, c in enumerate(frase) if c.lower() == letra.lower()]
    return posiciones


def validar_frase(frase: str) -> str:
    """Valida que la frase sea correcta (solo letras y espacios)."""
    frase = frase.strip()
    if frase is None or str(frase).strip() == "":
        raise ValueError("El campo no puede estar vacío.")

    if not frase.replace(" ", "").isalpha():
        raise ValueError("Error. La frase solo puede contener letras y espacios.")
    return frase


def validar_letra(letra: str) -> str:
    """
    Valida que la letra sea correcta
     (solo un caracter alfabético).
     """
    letra = letra.strip()
    if letra is None or str(letra).strip() == "":
        raise ValueError("El campo no puede estar vacío.")
    if not letra.isalpha():
        raise ValueError("Error. Solo puede contener letras.")
    if len(letra) != 1:
        raise ValueError("Error. Solo se puede ingresar una letra.")
    return letra


def main():
    while True:
        try:
            frase = validar_frase(input("Introduce una frase: "))
            letra = validar_letra(input("Introduce la letra que se desea buscar: "))

            resultado = encontrar_indices(frase, letra)

            if resultado:
                print(f"La letra '{letra}' aparece en la posición {resultado}")
            else:
                print(f"La letra '{letra}' no existe")

            break  # Salir del bucle después de un intento exitoso

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
