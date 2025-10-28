import unittest
from Calculadora import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def test_chain_operations(self):
        calc = Calculator()
        # (5 + 3) * 2 - 4 = 12
        result = calc.subtract(calc.multiply(calc.add(5, 3), 2), 4)
        self.assertEqual(result, 12)

if __name__ == "__main__":
    unittest.main()
