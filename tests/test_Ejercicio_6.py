import pytest

from Ejercicio_6 import validar_frase,validar_letra

def test_validar_frase():
    with pytest.raises(ValueError,match="El campo no puede estar vacío."):
        validar_frase("")
    with pytest.raises(ValueError, match="Error. La frase solo puede contener letras y espacios."):
        validar_frase("Hol123")

def test_validar_letra():
    with pytest.raises(ValueError,match="El campo no puede estar vacío."):
        validar_letra("")

    with pytest.raises(ValueError, match="Error. Solo puede contener letras."):
        validar_letra("3n")

    with pytest.raises(ValueError, match="Error. Solo se puede ingresar una letra."):
        validar_letra("ab")














