import pytest

from Ejercicio_3 import validar_contrasena

def test_validar_contrasena():
    with pytest.raises(ValueError,match="El campo no puede estar vacío."):
        validar_contrasena("")
    assert validar_contrasena("Aei1") == "Error: La contraseña debe tener mínimo 8 caracteres."
    assert validar_contrasena("12345678a") == "Error: La contraseña debe contener al menos una letra MAYÚSCULA."
    assert validar_contrasena("Aeiouaeoe") == "Error: La contraseña debe contener al menos un número."