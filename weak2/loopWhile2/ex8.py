# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите, какое количество элементов этой последовательности, равны ее наибольшему элементу.
firstElement = int(input())
max = firstElement
i = 1
while True:
    n = int(input())
    if(n>max):
        max = n
        i = 1
    elif(n==max):
        i = i + 1
    if(n==0):
        break
print(i)