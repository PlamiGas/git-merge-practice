Python
#Author: Проектная команда 
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
    print("Простой калькулятор")
    print("Сложение 5+3=", add(5, 3))
    print("Вычитание 10-4=", substract(10, 4))
    print("Умножение 6*7=", multiply(6, 7))
    print("Деление 15/3=", divide(15, 3))
