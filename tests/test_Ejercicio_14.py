import pytest

from Ejercicio_14 import validar_entrada

def test_validar_entrada():
    valido, resultado = validar_entrada("", set())
    assert valido == False
    assert resultado == "Error.No ingresaste nada. Escribe una letra."

    valido, resultado = validar_entrada("ab", set())
    assert valido == False
    assert resultado == "Error.Debes ingresar sólo una letra."

    valido, resultado = validar_entrada("5", set())
    assert valido == False
    assert resultado == "Error.Entrada inválida. Sólo se permiten letras (a-z)."

