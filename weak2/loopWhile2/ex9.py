# Последовательность Фибоначчи определяется так:
#
# [ F_0=0, F_1=1, ..., F_n=F_n-1+F_n-2. ]
#
# По данному числу n определите n-е число Фибоначчи Fn.
n = int(input())
i = 0
fib1 = 1
fib2 = 1
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
print(fib2)

