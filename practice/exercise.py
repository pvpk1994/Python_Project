'''
Importing Modules : Udemy Exercise
'''

from Addition.add import Addition  # Import Addition Class


class Calculator:

    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)

    @classmethod
    def subtract(cls, num1, num2):
        num3 = -num2
        return Addition.add(num1, num3)

    @classmethod
    def multiplication(cls, num1, num2):
        num3 = num1
        for i in range(0, num2-1):
            num1 = Addition.add(num1, num3)
        return num1

    @staticmethod
    def division(num1, num2):
        res = num1
        counter = 0
        while res >= num2:
            res = Calculator.subtract(res, num2)
            counter += 1
        return counter


adder = Calculator.add(3, 5)
print(f'Sum:{adder}')
print(f'Subtract:{Calculator.subtract(3,4)}')
print(f'Multiply:{Calculator.multiplication(7,4)}')
print(f'Division:{Calculator.division(36,6)}')


