#calculator.py
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b==0:
        return "Ошибка: Деление на ноль!"
    return a/b

if ___name___=="___main___":
    print("Результат простой калькулятор")
    print("Результат сложение 5+3=", add(5, 3))
    print("Результат вычитание 10-4=", substract(10, 4))
    print("Результат умножение 6*7=", multiply(6, 7))
    print("Результат деление 15/3=", divide(15, 3))
