#Crea un programa que calcule
# el precio de una entrada de cine basándose
# en la edad del cliente y si es estudiante


def verificar_edad(edad: int) -> int:
    """
    Recibe la edad y retorna el precio de lo que ingresan según la edad.
    Si no corresponde a ningún rango, retorna None.
    """


    if 1 < edad < 12:
        return 10000
    elif 12 <= edad <= 17:
        return 15000
    elif 18 <= edad <= 90:
        return 20000
    else:
        return None


def aplicar_descuento(precio: int, estudiante: str) -> int:
    """
    Recibe el precio y si la persona es estudiante ('si'), aplica un 10% de descuento.
    Retorna el precio final.
    """
    if estudiante == "si":
        return int(precio * 0.10)
    return precio  # Si no es estudiante, se retorna el precio normal


def pedir_edad(edad) :
    """
    Pide la edad al usuario y valida que:
    - No esté vacía
    - Sea un número entero
    - Sea positiva y no mayor a 90
    Retorna la edad válida.
    """

    while True:


        if edad is None or str(edad).strip() == "":
            raise ValueError ("El campo no puede estar vacío.")
            continue

        try:
            edad = int(edad)  # Convierte a entero
        except ValueError:
            return False

        if edad <= 0:
            return "Error: La edad debe ser positiva."
            continue
        if edad > 90:
            return "Error: La edad que ingresó excede el límite."
            continue


        return edad  # Si es válida, la devuelve


def pedir_estudiante(estudiante) -> str:
    """
    Pregunta si la persona es estudiante.
    Solo acepta 'si' o 'no' (en minúsculas).
    Retorna la respuesta válida.
    """
    while True:

        if estudiante not in ("si", "no"):  # Si responde algo distinto le especifica que debe ingresar
            return "Debe responder 'Si' o 'No'"
            continue
        return estudiante  # Devuelve la respuesta válida

def main():

    print("--- Bienvenido al Cine ---")
    edad = input("Ingrese la edad: ").strip()

    edad = pedir_edad(edad)  # Llamamos a pedir_edad(), devuelve un número válido
    if edad is False:
        print("Error: La edad debe ser un numero.")

    precio = verificar_edad(edad)  # Calcula el precio base según la edad

    if precio is None:  # Si no hay precio (edad fuera de rango)
        print("La edad que ingresó no es válida.")
        return

    estudiante = input("¿Es estudiante? Si/No: ").lower().strip()
    estudiante = pedir_estudiante()  # Pregunta si es estudiante
    precio_final = aplicar_descuento(precio, estudiante)  # Calcula el precio final

    print(f"El precio de su entrada es: ${precio_final:,}")



if __name__ == "__main__":
    main()

