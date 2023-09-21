# используются функции, которые могут выполнить повторяющиеся вычисления
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Ошибка. Деление на ноль"
    return num1 / num2

# Основной цикл калькулятора
while True:
    operation = input("Введите операцию (+, -, *, / или x для завершения): ")
    if operation == "x":
        break

    number1 = float(input("Введите первое число: "))
    number2 = float(input("Введите второе число: "))

    if operation == "+":
        result = add(number1, number2)
    elif operation == "-":
        result = subtract(number1, number2)
    elif operation == "*":
        result = multiply(number1, number2)
    elif operation == "/":
        result = divide(number1, number2)

    else:
        print("Ошибка: неизвестная операция")
        continue

    print("Результат:", result)

