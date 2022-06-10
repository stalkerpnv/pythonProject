# Даны произвольные действительные коэффициенты a, b, c. Решите уравнение ax2+bx+c=0.
import math

a = float(input())
b = float(input())
c = float(input())
d = b * b - 4 * a * c

if ((a == 0 and b == 0 and c == 0)):
    print("3")
elif(a == 0 and b == 0):
    print("0")
elif d < 0:
    print("0")
elif (a == 0):
    x = - c / b
    if (x.is_integer()):
        print("1", int(x))
    else:
        print("1", x)
elif (d == 0):
    x = -b / (2 * a)
    if (x.is_integer()):
        print("1", int(x))
    else:
        print("1", x)
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    if (x1 > x2):
        if (x1.is_integer() and x2.is_integer()):
            print("2", int(x2), int(x1))
        else:
            print("2", x2, x1)
    else:
        if (x1.is_integer() and x2.is_integer()):
            print("2", int(x1), int(x2))
        else:
            print("2", x1, x2)
