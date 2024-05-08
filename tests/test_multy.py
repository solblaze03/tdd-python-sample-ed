# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import mult

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_multi(self):

        assert mult(9,8 ) == 72
        assert mult(12,10 ) == 120
        assert mult(6,5 ) == 30
        
