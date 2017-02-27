d = {}
file = open('timings.txt')
for line in file:
    temp = line.split(",")
    name = temp[0].strip()
    time = float(temp[1].strip())
    d[name] = time

cubeHead = []
squareMaster = []
advanceTwister = []
interTurn = []
avgMover = []
pathetic = []
for k in d.keys():
    if d[k] < 9.99:
        cubeHead.append(k)
    elif d[k] >= 10 and d[k] < 19.99:
        squareMaster.append(k)
    elif d[k] >= 20 and d[k] < 29.99:
        advanceTwister.append(k)
    elif d[k] >= 30 and d[k] < 39.99:
        interTurn.append(k)
    elif d[k] >= 40 and d[k] < 59.99:
        avgMover.append(k)
    else:
        pathetic.append(k)


print cubeHead
print squareMaster
print advanceTwister
print interTurn
print avgMover
print pathetic

    for i in squareMaster:
        print i
    print advanceTwister
    for i in advanceTwister:
        print i
    print interTurn
        for i in cubeHead:
        print i
    print avgMover
        for i in cubeHead:
        print i
    print pathetic
        for i in cubeHead:
        print i