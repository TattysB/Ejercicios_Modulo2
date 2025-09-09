import pytest

from Ejercicio_9 import calcular_iva

def test_calcular_iva():
    productos=[{"nombre":"camisa","precio":2000},
               {"nombre":"pantalón","precio":1000},]

    resultado=calcular_iva(productos)
    esperado={"camisa":2380.0,"pantalón":1190.0}
    assert resultado == esperado



