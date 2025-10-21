import unittest
from Manejo_de_pruebas.Calculadora import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def test_operation_chain(self):
        calc = Calculator()
        # (2 + 3) * 4 / 2 = 10
        result = calc.divide(calc.multiply(calc.add(2, 3), 4), 2)
        self.assertEqual(result, 10)

if __name__ == "__main__":
    unittest.main()
