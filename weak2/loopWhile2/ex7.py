# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите значение второго по величине элемента в этой последовательности,
# то есть элемента, который будет наибольшим, если из последовательности удалить наибольший элемент.
#
# Формат ввода
# Вводится последовательность целых чисел, оканчивающаяся числом 0
# (само число 0 в последовательность не входит, а служит как признак ее окончания).
#
# Формат вывода
# Выведите ответ на задачу.

firstElement = int(input())
secondElement = int(input())
if(firstElement>secondElement):
    firstMax = firstElement
    secondMax = secondElement
else:
    firstMax = secondElement
    secondMax = firstElement
while True:
    n = int(input())
    if (n == 0):
        break
    if(n>firstMax):
        secondMax = firstMax
        firstMax = n
    elif(n>secondMax):
        secondMax = n
print(secondMax)
