import pytest

from Ejercicio_4 import jugar_ronda

def test_jugar_ronda():
    assert jugar_ronda("","piedra") == "El campo no puede estar vacío."
    assert jugar_ronda("hoja","piedra") == "Error. Opción invalida, intente nuevo."
