import Epic

def readFlavors(filename):
    file = open(filename)
    flavorList = []
    for flavor in file:
        flavorList.append(flavor.strip())
    return flavorList

def countInStock(instock, flavors):
    count = 0
    for f in flavors:
        if (f.upper() in instock):
            count += 1
    return count
    
def main():
    instock = ['VANILLA', 'CHOCOLATE', 'STRAWBERRY']
    flavs = readFlavors('flavors.txt')
    c = countInStock(instock, flavs)
    print 'We have %s of your flavors in stock!' % c
    
main()