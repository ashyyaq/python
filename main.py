# используется библиотека math для выполнения математических операций
import math
print("Калькулятор")
while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Синус")
    print("6. Косинус")
    print("7. Тангенс")
    print("8. Квадратный корень")
    print("9. Возведение в степень")
    print("10. Факториал")
    print("0. Выход")

    choice = input("Введите номер операции (0-10): ")

# выход из калькулятора осуществляется номером операции "0"
    if choice == '0':
        print("Выход")
        break

# если выбраны номеры операций "1, 2, 3, 4", то выполняются сложение, вычитание, умножение или деление в зависимости от выбранного номера
    elif choice in ['1', '2', '3', '4']:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            result = num1 + num2
            print("Результат: ", result)
        elif choice == '2':
            result = num1 - num2
            print("Результат: ", result)
        elif choice == '3':
            result = num1 * num2
            print("Результат: ", result)
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print("Результат: ", result)
            else:
                print("Деление на ноль невозможно.")

# если выбраны номеры операций "5, 6, 7", то выполняются тригонометрические операции
    elif choice in ['5', '6', '7']:
        angle = float(input("Введите значение угла в градусах): "))
        radian = math.radians(angle)

        if choice == '5':
            result = math.sin(radian)
            print("Результат: ", result)
        elif choice == '6':
            result = math.cos(radian)
            print("Результат: ", result)
        elif choice == '7':
            result = math.tan(radian)
            print("Результат: ", result)
        else:
            print("Некорректный выбор операции. Попробуйте еще раз.")
    else:
        print("Ошибка! Введите числовое значение.")

# если выбрано "8", то выполняется извлечение из корня
elif choice == "8":
        num = float(input("Введите число для извлечения квадратного корня: "))
        result = math.sqrt(num)
        print("Результат: ", result)
        else:
        print("Ошибка! Квадратный корень отрицательного числа не определен.")

# если выбрано "9", то выполняется возведение в степень
    elif choice == "9":
        base = input("Введите основание: ")
        exponent = input("Введите показатель степени: ")
        base = float(base)
        exponent = float(exponent)
        result = base ** exponent
        print("Результат:", result)

# если выбрано "10", то выполняется вычисление факториала выбранного числа
    elif choice == "10":
        num = float(input("Введите число для вычисления факториала: "))
        result = math.factorial(int(num))
        print("Результат:", result)

    else:
        print("Некорректный ввод. Попробуйте ещё раз.")

