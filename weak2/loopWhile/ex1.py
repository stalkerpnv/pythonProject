# По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
#
# Формат ввода
# Вводится натуральное число.
#
# Формат вывода
# Выведите ответ на задачу.
N = int(input())
i = 1
while i*i <= N:
    print(i * i)
    i = i + 1