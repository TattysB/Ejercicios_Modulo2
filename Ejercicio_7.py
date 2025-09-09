#Dadas dos listas, una con nombres de estudiantes
# y otra con sus respectivas notas finales, crea
# una función que las combine para generar un diccionario.
# Las claves serán los nombres y los valores las notas:

def combinar_listas(nombre: list, nota: list) -> dict:
    """
    Combina las dos listas en un diccionario usando zip.

    Args:
        nombre (list): Lista de nombres
        nota (list): Lista de notas

    Returns:
        dict: Diccionario con los nombres como claves y las notas como valores
    """
    return dict(zip(nombre, nota))


def validar_cantidad(cantidad: str) -> int:
    """Valida que la cantidad ingresada sea un número entero positivo."""
    cantidad = cantidad.strip()
    if cantidad == "":
        raise ValueError("El campo no puede estar vacío.")

    if not cantidad.isdigit():
        raise ValueError("Error. Solo puedes ingresar números enteros.")
    return int(cantidad)


def validar_nombre(nombre: str) -> str:
    """Valida que el nombre solo contenga letras y no esté vacío."""
    nombre = nombre.strip()
    if nombre == "":
        raise ValueError("Error. El campo no puede estar vacío.")

    if not nombre.isalpha():
        raise ValueError("Error. Solo puede contener letras en el campo nombre.")
    return nombre


def validar_nota(nota: str) -> float:
    """Valida que la nota sea un número entre 0 y 5."""
    nota = nota.strip()
    if nota == "":
        raise ValueError("El campo no puede estar vacío.")

    try:
        nota_f = float(nota)
    except ValueError:
        raise ValueError("Error. Debes ingresar un número válido.")

    if not (0 <= nota_f <= 5):
        raise ValueError("Error. La nota debe estar entre 0 y 5.")
    return nota_f


def main():
    nombres = []
    notas = []

    # Ingreso de cantidad de estudiantes
    while True:
        try:
            cantidad = validar_cantidad(input("¿Cuántos estudiantes desea ingresar: "))
            break
        except ValueError as e:
            print(e)

    # Ingreso de nombres y notas
    for i in range(cantidad):
        while True:
            try:
                nombre = validar_nombre(input(f"Ingrese el nombre del estudiante {i+1}: "))
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                nota = validar_nota(input(f"Ingrese la nota del estudiante {nombre}: "))
                break
            except ValueError as e:
                print(e)

        nombres.append(nombre)
        notas.append(nota)

    diccionario = combinar_listas(nombres, notas)

    print("\nReporte de notas:")
    for nombre, nota in diccionario.items():
        print(f"El estudiante {nombre} tiene una nota de {nota}")


if __name__ == "__main__":
    main()
