myDict = {}
while True:
    try:
        seq = map(str, input().split())
        for word in seq:
            print(myDict.get(word, 0), sep=' ', end=' ')
            myDict[word] = myDict.get(word, 0) + 1
    except EOFError:
        break
    # print(mySet.count(word), end=' ')
    # mySet.append(word)
