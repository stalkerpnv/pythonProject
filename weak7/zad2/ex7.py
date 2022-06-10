myDict ={}
while True:
    try:
        line = list(map(str, input().split()))
        #nameParty = str(line[0:-1]).replace(',',' ')
        nameParty = ' '.join(map(str, line[0:-1]))
        votes = line[-1]
        myDict[nameParty] = myDict.get(nameParty,0) + int(votes)
    except EOFError:
        break
sumVotes = 0
for nameParty, votes in sorted(myDict.items()):
    sumVotes = sumVotes + votes
firstIzPravo = sumVotes/450
print(firstIzPravo)

places = 450
for nameParty, votes in sorted(myDict.items()):
   myDict[nameParty] = int(myDict[nameParty]/firstIzPravo)
   places = places - int(myDict[nameParty]/firstIzPravo)
for nameParty, votes in sorted(myDict.items()):
    print(nameParty, votes)
print(places)