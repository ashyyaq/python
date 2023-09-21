def rectangle_area(width, height):
    area = width * height
    return area
width = float(input("Введите ширину: "))
height = float(input("Введите высоту: "))
result = rectangle_area(width, height)
print ("Результат: ", result)