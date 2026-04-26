import pytest
from converter import *

class TestConverter:
    def test_celsius_to_fahrenheit(self):
        assert celsius_to_fahrenheit(100) == 212.0
        assert fahrenheit_to_celsius(212) == 100.0

    def test_km_to_miles(self):
        assert km_to_miles(1) == 0.62
        assert miles_to_km(1) == 1.61

    def test_peso_y_otros(self):
        # Estas pruebas cubren las líneas que faltaban (Missing)
        assert kg_to_libras(1) == 2.2
        assert libras_to_kg(1) == 0.45
        # Si tienes Kelvin o gramos, agrega un assert similar aquí