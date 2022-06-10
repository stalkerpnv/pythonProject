# Если точка принадлежит области (область включает границы), выведите слово YES, иначе выведите слово NO.
# Решение должно содержать функцию IsPointInArea(x, y), возвращающую True, если точка принадлежит области и False,
# если не принадлежит. Основная программа должна считать координаты точки, вызвать функцию IsPointInArea
# и в зависимости от возвращенного значения вывести на экран необходимое сообщение.
# Функция IsPointInArea не должна содержать инструкцию if.

def IsPointInArea(x, y):
    condOne = ((x + 1) ** 2 + (y - 1) ** 2 <= 4) and (y - 2 * x >= 2 and y >= -x)
    condTwo = ((x + 1) ** 2 + (y - 1) ** 2 >= 4) and (y - 2 * x <= 2 and y <= -x)
    return condOne or condTwo


x = float(input())
y = float(input())
if (IsPointInArea(x, y)):
    print("YES")
else:
    print("NO")
