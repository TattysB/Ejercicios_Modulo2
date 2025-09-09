import pytest

from Ejercicio_15 import validar_coordenada,validar_disparo_repetido

def test_validar_coordenada():

    assert validar_coordenada("AA")  is False
    assert validar_coordenada("A1") is True

def test_validar_disparo_repetido():
    disparos = {(0, 0), (1, 2), (4, 4)}  # disparos ya hechos
    assert validar_disparo_repetido((0, 0), disparos) is True  # repetido
    assert validar_disparo_repetido((2, 3), disparos) is False  # nuevo



