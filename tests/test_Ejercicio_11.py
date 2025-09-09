import pytest

from Ejercicio_11 import validar_vacio,validar_numerico,validar_longitud

def test_validar_vacio():
    with pytest.raises(ValueError,match="El campo no puede estar vacío."):
        validar_vacio("")

def test_validar_numerico():
    with pytest.raises(ValueError,match="Error. La cédula solo puede contener números."):
        validar_numerico("ad*")

def test_validar_longitud():

    with pytest.raises(ValueError,match="Error. El número de cédula tiene que tener entre 10 y 11 dígitos."):
        validar_longitud("123")