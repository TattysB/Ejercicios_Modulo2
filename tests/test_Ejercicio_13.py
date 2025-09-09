import pytest

from Ejercicio_13 import validar_entrada,validar_biblioteca,validar_sotano

def test_validar_entrada():
    assert validar_entrada("norte") == "biblioteca"
    assert validar_entrada("este") == "sotano"
    assert validar_entrada("salir") == "salir"
    assert validar_entrada("xyz") == "Opción inválida. Intenta de nuevo."

def test_validar_biblioteca():

    assert validar_biblioteca("abrir cofre") == "ganaste"
    assert validar_biblioteca("sur") == "entrada"
    assert validar_biblioteca("xyz") == "Opción inválida. Intenta de nuevo."

def test_validar_sotano():

    assert validar_sotano("") == "perdiste"
    assert validar_sotano("oeste") == "entrada"
