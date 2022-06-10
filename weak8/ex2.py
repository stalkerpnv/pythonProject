mySet = set()
while True:
    try:
        line = input().split()
        for i in range(len(line)):
            if line[i] not in mySet:
                mySet.add(line[i])
    except EOFError:
        break
print(len(mySet))