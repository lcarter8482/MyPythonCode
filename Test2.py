d = {}

for line in open('birds.txt'):
    temp = line.split(",")
    bird = temp[0].strip()
    timesSeen = int(temp[1].strip())
    if bird in d:
        d[bird] = d[bird] + timesSeen
    else:
        d[bird] = timesSeen
print d