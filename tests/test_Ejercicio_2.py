import pytest

from Ejercicio_2 import pedir_comando

def test_pedir_comando():

    with pytest.raises(ValueError,match="El campo no puede estar vacío."):
        pedir_comando("")

    assert pedir_comando("5") == 'Error: número fuera de rango.'
    assert pedir_comando("-*") == " Error: Solo se aceptan letras o números válidos del menú."




