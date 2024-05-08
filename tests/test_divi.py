# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import divi

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class DiviTestClass:

    # Test para la operación suma
    def test_divi(self):

        assert divi(8,2 ) == 4
        assert divi(5,1 ) == 5
        assert divi(81,9 ) == 9
        
