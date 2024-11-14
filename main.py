def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль."
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Ошибка: корень определён только для неотрицательных чисел."
    return x ** (1/2)

def modulus(x, y):
    return x % y

def absolute(x):
    return x if x >= 0 else -x

def factorial(x):
    if x < 0:
        return "Ошибка: факториал определён только для неотрицательных чисел."
    if not x.is_integer():
        return "Ошибка: факториал можно вычислить только для целых чисел."
    x = int(x)
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def calculate(operation, x, y=None):
    if operation == '+':
        return add(x, y)
    elif operation == '-':
        return subtract(x, y)
    elif operation == '*':
        return multiply(x, y)
    elif operation == '/':
        return divide(x, y)
    elif operation == '^':
        return power(x, y)
    elif operation == '%':
        return modulus(x, y)
    elif operation == 'sqrt':
        return sqrt(x)
    elif operation == 'abs':
        return absolute(x)
    elif operation == '!':
        return factorial(x)
    else:
        return "Ошибка: неверная операция"

def get_operation():
    while True:
        operation = input("Введите операцию (+, -, *, /, ^, %, sqrt, abs, !): ")
        if operation in ["+", "-", "*", "/", "^", "%", "sqrt", "abs", "!"]:
            return operation
        else:
            print("Неверный ввод. Попробуйте ещё раз.")

def get_numbers(operation):
    if operation in ["+", "-", "*", "/", "^", "%"]:
        while True:
            try:
                num1 = float(input("Введите первое число(в формате 0.0): "))
                num2 = float(input("Введите второе число(в формате 0.0): "))
                return num1, num2
            except ValueError:
                print("Ошибка: введите действительные числа.")
    elif operation in ["sqrt", "abs", "!"]:
        while True:
            try:
                num1 = float(input("Введите число(в формате 0.0): "))
                return num1, None
            except ValueError:
                print("Ошибка: введите действительное число.")

def get_user_input():
    operation = get_operation()
    num1, num2 = get_numbers(operation)
    return operation, num1, num2

# Основная программа
operation, num1, num2 = get_user_input()
result = calculate(operation, num1, num2)
print("Результат:", result)
