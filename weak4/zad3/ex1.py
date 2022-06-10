# Возведение в степень
# Дано действительное положительное число a и целое неотрицательное число n.
# Вычислите an не используя циклы и стандартную функцию pow, а используя рекуррентное соотношение an=a⋅ an-1.
# Решение оформите в виде функции power(a, n).
# Формат ввода
# Вводятся действительное положительное число a и целое неотрицательное число n.
def power(a, n):
    if (n == 0):
        return 1
    if (n == 1):
        return a
    return a * power(a, n - 1)

a = float(input())
n = int(input())
result = power(a, n)
if result ==1:
    print(result)
elif result.is_integer():
    print(int(result))
else:
    print(result)
