import time
from Calculadora import Calculator

def test_performance():
    calc = Calculator()
    start = time.time()
    for _ in range(500000):
        calc.add(1, 1)
        calc.multiply(2, 2)
        calc.divide(10, 2)
    end = time.time()
    print(f"Tiempo total: {end - start:.4f} segundos")

if __name__ == "__main__":
    test_performance()
