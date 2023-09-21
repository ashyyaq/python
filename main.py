def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

num = int(input("Введите число: "))
result = is_even(num)
print(result)