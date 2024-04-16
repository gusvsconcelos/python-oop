from math import sqrt


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return 'Cannot divide by zero'

    def expo(self, x, y):
        return x ** y

    def root(self, x):
        return sqrt(x)


calculator = Calculator()

result = calculator.add(7, 5)
print("7 + 5 =", result)

result = calculator.subtract(34, 21)
print("34 - 21 =", result)

result = calculator.multiply(54, 2)
print("54 * 2 =", result)

result = calculator.divide(144, 2)
print("144 / 2 =", result)

result = calculator.divide(45, 0)
print("45 / 0 =", result)

result = calculator.expo(2, 3)
print("2^3 =", result)

result = calculator.root(9)
print("square root of 9 =", result)
