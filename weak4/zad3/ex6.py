# Даны два натуральных числа n и m. Сократите дробь (n / m), то есть выведите два других числа p и q таких, что (n / m) = (p / q) и дробь (p / q) — несократимая.
# Решение оформите в виде функции ReduceFraction(n, m), получающая значения n и m и возвращающей кортеж из двух чисел.

def  gcd(a, b):
    if b==0:
        return a
    return gcd(b,a%b)

def reduceFraction(n, m):
    div = gcd(n,m)
    return n//div, m//div


n = int(input())
m = int(input())
p, q = reduceFraction(n, m)
print(p, q)