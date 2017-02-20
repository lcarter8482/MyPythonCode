import Epic
# Reads the specified file and returns a dictionary of how many times seen
def countBirds(filename):
    d = {}
    file = open(filename)
    for line in file:
        temp = line.split(",")
        bird = temp[0].strip()
        timesSeen = int(temp[1].strip())
        if bird in d:
            d[bird] = d[bird] + timesSeen
        else:
            d[bird] = timesSeen
    return d

# Asks the user to enter a bird name and then looks up the sighting count
def askUser(d):
    count = 0
    b = Epic.userString("Enter a bird name: ")
    if b in d.keys():
        count = d[b]
    return count

def main():
    birds = countBirds("birds.txt")
    birdCount = askUser(birds)
    print "I have seen that bird %s time(s)." % birdCount
    
main()