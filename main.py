from Calculadora import Calculator

def main():
    try:
        a = float(input("Ingrese un número a: "))
        b = float(input("Ingrese un número b: "))
        Op = input("Ingrese la operación (+, -, *, /): ")

        calc = Calculator()

        if Op == '+':
            print(f"Resultado: {calc.add(a, b)}")
        elif Op == '-':
            print(f"Resultado: {calc.subtract(a, b)}")
        elif Op == '*':
            print(f"Resultado: {calc.multiply(a, b)}")
        elif Op == '/':
            try:
                print(f"Resultado: {calc.divide(a, b)}")
            except ValueError as e:
                print(e)
        else:
            print("Operación no válida")

    except ValueError:
        print("Entrada no válida. Por favor ingrese números válidos.")

if __name__ == "__main__":
    main()
