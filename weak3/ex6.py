n = int(input())
x = round(float(input()), 5)
a = round(float(input()), 5)
result = a
i = n
while i != 0:
    a =  round(float(input()), 5)
    result = result * x
    result = result + a
    i = i - 1
if(result.is_integer()):
    print(int(result))
else:
    print(result)

