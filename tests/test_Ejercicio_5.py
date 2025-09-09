import pytest

from Ejercicio_5 import validar_numero

def test_validar_numero():
    with pytest.raises(ValueError, match="El campo no puede estar vacío."):
        validar_numero("")
    with pytest.raises(ValueError, match="Debe ingresar un número entero."):
        validar_numero("abc")

    with pytest.raises(ValueError, match="Error. El número tiene que estar dentro de -1000 y 1000."):
        validar_numero("2000")



