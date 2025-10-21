import time
from Manejo_de_pruebas.Calculadora import Calculator

def test_performance():
    calc = Calculator()
    start = time.time()
    for _ in range(1_000_000):
        calc.add(1, 2)
        calc.multiply(3, 4)
        calc.divide(10, 5)
    end = time.time()
    print(f"Tiempo total: {end - start:.4f} segundos")

if __name__ == "__main__":
    test_performance()
