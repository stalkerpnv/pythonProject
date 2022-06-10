names = input().split()
cities = input().split()
for i in range(len(cities)):
    if(cities[i][0]=='T'):
        print(names[i], 'comes from', cities[i])