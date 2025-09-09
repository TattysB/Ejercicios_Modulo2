import pytest

from Ejercicio_1 import verificar_edad, pedir_edad, pedir_estudiante

def test_verificar_edad():
    assert verificar_edad(11) == 10000
    assert verificar_edad(14) == 15000
    assert verificar_edad(50) == 20000

def test_pedir_edad():
    assert pedir_edad(-5) == "Error: La edad debe ser positiva."
    assert pedir_edad(95) == "Error: La edad que ingresó excede el límite."
    with pytest.raises(ValueError,match="El campo no puede estar vacío."):
        pedir_edad("")
    assert pedir_edad("ll") == False


def test_pedir_estudiante():

    assert pedir_estudiante("quizas") == "Debe responder 'Si' o 'No'"





