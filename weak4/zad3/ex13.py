# Только квадраты
# Напишите программу, которая выбирает их полученной последовательности квадраты целых чисел выводит их в обратном порядке. Использовать массив для хранения последовательности не разрешается.
#
# Формат ввода
# Во входных строках записаны целые числа, по одному в каждой строке. В последней строке записано число 0.
#
# Формат вывода
# Программа должна вывести элементы полученной последовательности, которые представляют собой квадраты целых чисел,
# в обратном порядке в одну строчку, разделив их пробелами. Если таких нет, программа должна вывести число 0.
k = 0
def fillCons(x):
    global k
    if x != 0:
        fillCons(int(input()))
    if (x ** 0.5).is_integer() and x != 0:
        print('', x, end='')
        k = k + 1

fillCons(int(input()))
if(k==0):
    print('0')