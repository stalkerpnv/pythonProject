# Последовательность состоит из натуральных чисел, не превосходящих 109, и завершается числом 0.
# Определите значение наибольшего элемента последовательности.
#
# Формат ввода
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность
# не входит, а служит как признак ее окончания).
#
# Формат вывода
# Выведите ответ на задачу.
firstNumber = int(input())
max = firstNumber
x = -1
while(x!=0):
    x = int(input())
    if max < x:
        max = x
print(max)