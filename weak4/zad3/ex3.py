# Возводить в степень можно гораздо быстрее, чем за n умножений!
# Для этого нужно воспользоваться следующими рекуррентными соотношениями: an=(a2)n/2 при четном n,
# an=a⋅ an-1 при нечетном n. Реализуйте алгоритм быстрого возведения в степень.
# Если вы все сделаете правильно, то сложность вашего алгоритма будет O(logn).

def power(a, n):
    return (1 if n == 0
            else power(a * a, n // 2) if n % 2 == 0
            else a * power(a, n - 1))

a = float(input())
n = int(input())
result = power(a, n)
if result ==1:
    print(result)
elif result.is_integer():
    print(int(result))
else:
    print(result)