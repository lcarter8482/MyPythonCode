#reading specified file
def readData(filename):
    l = []
    file = open(filename)
    for item in file:
        l.append(float(item.strip()))
    return l

#calculating average of a list
def getAverage(l):
    total = 0
    for index in range(len(l)):
        total += l[index]
    return total / len(l)

#counting number of speeders over designated max speed
def countSpeeders(l, maxSpeed):
    count = 0
    for index in l:
        if index > maxSpeed:
            count += 1
    return count

def main():
    rush = readData('data-rush.txt')
    notRush = readData('data-not-rush.txt')
    rushAvg = getAverage(rush)
    notRushAvg = getAverage(notRush)
    rushSpeeders = countSpeeders(rush, 69)
    notRushSpeeders = countSpeeders(notRush, 69)
    
    #calculating speeding fines
    rushFine = rushSpeeders * 150
    notRushFine = notRushSpeeders * 100
   
    print 'The average speed during rush hour was %.2f' % rushAvg
    print 'The average speed not during rush hour was %.2f' % notRushAvg
    print 'There were %s speeders during rush hour.  Total fine = $%s' % (rushSpeeders, rushFine)
    print 'There were %s speeders not during rush hour.  Total fine = $%s' % (notRushSpeeders, notRushFine)

main()