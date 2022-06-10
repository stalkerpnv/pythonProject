def get_retakes(myDict):
    listS = list()
    for key in myDict:
        l = list(myDict[key])
        for i in l:
            if i < 4:
                listS.append(key)
            continue
        listS.sort()
    return listS



myDict = dict({
    'Harry Potter': [7, 6, 8, 3, 6],
    'Hermione Granger': [10, 10, 9, 10, 10, 9, 9],
    'Ron Weasley': [6, 5, 7, 4, 5],
    'Ginny Weasley': [9, 7, 3]
})
print(get_retakes(myDict))

