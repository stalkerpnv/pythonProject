def power(a, n):
    if n == 0:
        return 1
    i = 0
    result = 1
    while i < abs(n):
        result = result * a
        i = i + 1
    if n < 0:
        return 1 / result
    else:
        return result


a = float(input())
n = int(input())
result = power(a, n)
if result ==1:
    print(result)
elif result.is_integer():
    print(int(result))
else:
    print(result)

