import pytest

from Ejercicio_12 import lanzar_dados

def test_lanzar_dados():
    for _ in range(100):
        resultado = lanzar_dados()
        assert 2 <= resultado <= 12  # validamos el rango correcto
