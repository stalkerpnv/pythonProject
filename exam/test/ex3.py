container = {'one':(1,2),'two':(4,6,3),'three':(7,9)}
n= int(input())
for elem in container:
    if container[elem][0] < n:
        print(container[elem][-1])