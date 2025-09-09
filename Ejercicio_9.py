#Tienes una lista de productos, donde cada producto
# es un diccionario: [{"nombre": "Camisa", "precio": 50000},
# {"nombre": "Pantalón", "precio": 80000}]:
#Usa una dictionary comprehension para crear un nuevo
# diccionario donde los nombres de los productos sean las claves
# y los precios con un 19% de IVA incluido sean los valores
def calcular_iva(productos):
    """
        Crear un nuevo diccionario usando dictionary comprehension
        donde:
         * Las claves serán los nombres de los productos.
         * Los valores serán los precios con un 19% de IVA incluido.

        """
    # Dictionary comprehension y  recorre cada producto en la lista y construye un diccionario nuevo
    producto_iva={
            producto["nombre"]: producto["precio"] * 1.19
            for producto in productos
           }
    return producto_iva

def main():


    productos=[
        {"nombre": "Camisa", "precio": 5000},
        {"nombre": "Pantalón", "precio": 80000}
        ]
    producto_iva = calcular_iva(productos)

    print("Productos originales:", productos)
    print("Productos con IVA:", producto_iva)

if __name__ == "__main__":
    main()
