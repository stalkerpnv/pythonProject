# Периметр треугольника
# Напишите функцию, вычисляющую длину отрезка по координатам его концов.
# С помощью этой функции напишите программу, вычисляющую периметр треугольника по координатам трех его вершин.
# Формат ввода
# На вход программе подается 6 целых чисел — координат x1, y1,x2,y2, x3,y3 вершин треугольника.
# Формат вывода
# Выведите значение периметра этого треугольника с точностью до 6 знаков после десятичной точки.
import math
def distance(x1,y1,x2,y2):
    return math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
p = distance(x1,y1,x2,y2) + distance(x2,y2,x3,y3) + distance(x1,y1,x3,y3)
print(round(p,6))
