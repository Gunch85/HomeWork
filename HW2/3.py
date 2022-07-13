import math

print("Введите координаты точки и радиус круга: ")
x = float(input("x = "))
y = float(input("y = "))
r = float(input("r = "))

hypotenuse = math.sqrt(x ** 2 + y ** 2)

if hypotenuse <= r:
    print("Точка принадлежит кругу")
else:
    print("Точка вне круга")