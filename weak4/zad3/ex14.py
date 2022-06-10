import math


def findNumbers(x, p, q):
    b = int(math.pow(x, 1/p))
    if x - math.pow(x, p) == 0:
        return str(b)
    if q == 1:
        return 0
    if findNumbers(x - math.pow(x, p), p, q - 1) != 0:
        b -= 1
        if b <= 0:
            return 0
    return findNumbers(x - math.pow(x, p), p, q - 1) + ' ' + str(b)


n = int(input())

print(findNumbers(n, 3, 7))
