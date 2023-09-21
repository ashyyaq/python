def sum_digits(number):
    number_str = str(number)
    digit_sum = 0
    for digit in number_str:
        digit_sum += int(digit)
    return digit_sum

num = int(input("Введите положительное целое число: "))
result = sum_digits(num)
print(result)
