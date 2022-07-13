# Найти площадь и периметр прямоугольного треугольника
import math

AB = input("Длина первого катета: ")
AC = input("Длина второго катета: ")

AB = float(AB)
AC = float(AC)
# math.sqrt(X) - квадратный корень из X.
BC = math.sqrt(AB ** 2 + AC ** 2)
S = (AB * AC) / 2
P = AB + AC + BC
print(P)
