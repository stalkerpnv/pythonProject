myList = list(map(int, input().split()))
myList.sort()
value = 0
for i in range(len(myList)):
    if myList[i] % 2 == 1:
        value = myList[i]
        break
print(value)
