# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import resta

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class RestaTestClass:

    # Test para la operación suma
    def test_resta(self):

        assert resta(10,8 ) == 2
        assert resta(52,10 ) == 42
        assert resta(89,30 ) == 59
        
