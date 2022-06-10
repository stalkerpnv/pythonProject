myDict = {}
while True:
    try:
        line = list(map(str,input().split()))
        for word in line:
            myDict[word] = myDict.get(word,0) + 1
    except EOFError:
        break
max =max(myDict.values())
most_frequent = [k for k, v in myDict.items() if v == max]
print(min(most_frequent))