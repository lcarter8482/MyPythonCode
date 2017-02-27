#reading in the file and returns as dictionary
def rubiksTimes(filename):
    d = {}
    file = open(filename)
    for line in file:
        temp = line.split(",")
        name = temp[0].strip()
        time = float(temp[1].strip())
        d[name] = time
    return d
    
#determines which category each name will be in from designated start and stop  
def timeCategories(d, start, stop):
    l = []
    for k in d.keys():
        if d[k] >= start and d[k] < stop:
            l.append(k)
    return l

def main():
    rubiks = rubiksTimes('timings.txt')
    cubeHead = timeCategories(rubiks, 0, 9.99)
    squareMaster = timeCategories(rubiks, 10, 19.99)
    advanceTwister = timeCategories(rubiks, 20, 29.99)
    interTurn = timeCategories(rubiks, 30, 39.00)
    avgMover = timeCategories(rubiks, 40, 59.99)
    pathetic = timeCategories(rubiks, 60, 2000)


    print 'Cube Head (0 - 9.99):'
    for i in cubeHead:
        print "        " + i
    print '\nSquare Master (10 - 19.99):'
    for i in squareMaster:
        print "        " + i
    print '\nAdvance Twister (20 - 29.99):'
    for i in advanceTwister:
        print "        " + i
    print '\nIntermediate Turner (30 - 39.99):'
    for i in interTurn:
        print "        " + i
    print '\nAverage Mover (40 - 59.99):'
    for i in avgMover:
        print "        " + i
    print '\nPathetic (60 and beyond):'
    for i in pathetic:
        print "        " + i
    
main()