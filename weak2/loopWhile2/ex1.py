# По данному натуральном n вычислите сумму 12+22+32+...+n2.
#
# Формат ввода
# Вводится натуральное число.
#
# Формат вывода
# Выведите ответ на задачу.

n = int(input())
sum = 0
i = 1
while i <=n:
    sum = sum + i*i
    i = i+1
print(sum)