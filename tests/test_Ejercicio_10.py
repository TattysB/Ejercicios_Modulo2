import types

from Ejercicio_10 import mover_matriz

def test_mover_matriz():
    matriz =[[1,2,3],[4,5,6],[7,8,9]]
    esperado =[[1,4,7],[2,5,8],[3,6,9]]

    assert mover_matriz(matriz) == esperado
