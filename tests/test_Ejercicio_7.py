import pytest

from Ejercicio_7 import validar_cantidad,validar_nombre,validar_nota

def test_validar_cantidad():
    with pytest.raises(ValueError,match="El campo no puede estar vacío."):
        validar_cantidad("")
    with pytest.raises(ValueError,match="Error. Solo puedes ingresar números enteros."):
        validar_cantidad("-3")

def test_validar_nombre():
    with pytest.raises(ValueError,match="El campo no puede estar vacío."):
        validar_nombre("")

    with pytest.raises(ValueError,match="Error. Solo puede contener letras en el campo nombre."):
        validar_nombre("123")

def test_validar_nota():
    with pytest.raises(ValueError,match="El campo no puede estar vacío."):
        validar_nota("")

    with pytest.raises(ValueError,match="Error. Debes ingresar un número válido."):
        validar_nota("1q")

    with pytest.raises(ValueError,match="Error. La nota debe estar entre 0 y 5."):
        validar_nota("6")

