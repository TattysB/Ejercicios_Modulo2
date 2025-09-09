import pytest

from Ejercicio_8 import obtener_positivos,obtener_cuadrados,obtener_etiquetas

def test_obtener_positivos():
    assert obtener_positivos([55, -10, -15, 20,]) == [55,20]

def test_obtener_cuadrados():
    assert obtener_cuadrados([-6, 10,]) ==[36,100]

def test_obtener_etiquetas():
    assert obtener_etiquetas([-6,2,3,-9]) == ["negativo", "positivo","positivo","negativo"]
