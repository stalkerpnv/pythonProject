import math

a = float(input())
b = float(input())
c = float(input())
d = b * b - 4 * a * c
if d == 0:
    x = -b / (2 * a)
    if (x.is_integer()):
        print(int(x))
    else:
        print(x)
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    if(x1>x2):
        if (x1.is_integer() and x2.is_integer()):
            print(int(x2), int(x1))
        else:
            print(x2, x1)

    else:
        if (x1.is_integer() and x2.is_integer()):
            print(int(x1), int(x2))
        else:
            print(x1, x2)

