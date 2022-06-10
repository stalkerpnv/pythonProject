# Теорема Лагранжа утверждает, что любое натуральное число можно представить в виде суммы четырех
# точных квадратов.По данному числу n найдите такое представление: напечатайте от 1 до 4 натуральных чисел,
# квадраты которых дают в сумме данное число.

# a**2 + b**2 + c**2 + d**2 = n
def findNumbers(n, pow, q):
    a = int(n ** 0.5) -1
    if n - a ** 2 == 0:
        return str(a)
    if q == 1:
        return 0
    while findNumbers(n - a ** pow, pow, q - 1) == 0:
        a = a - 1
        if a <= 0:
            return 0
    return findNumbers(n - a ** pow, pow, q - 1) + " " + str(a)




def lagrange(x, pow, q):
    b = int(x ** (1 / pow))
    if x - b ** pow == 0:
        return str(b)
    if q == 1:
        return 0
    if lagrange(x - b ** pow, pow, q - 1) != 0:
        b -= 1
        if b <= 0:
            return 0
    return lagrange(x - b ** pow, pow, q - 1) + ' ' + str(b)


# n = int(input())
#
# print(lagrange(n, 2, 4))

n = int(input())
print(findNumbers(n, 2, 4))
