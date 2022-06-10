from collections import Counter

myDict = {}
while True:
    try:
        line = list(map(str, input().split()))
        for word in line:
            myDict[word] = myDict.get(word, 0) + 1
    except EOFError:
        break

counter = Counter(myDict)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))