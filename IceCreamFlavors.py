import Epic

def getFlavors():
    flavorList = []
    flavorList.append(Epic.userString('Enter flavor 1: '))
    flavorList.append(Epic.userString('Enter flavor 2: '))
    flavorList.append(Epic.userString('Enter flavor 3: '))
    flavorList.append(Epic.userString('Enter flavor 4: '))
    flavorList.append(Epic.userString('Enter flavor 5: '))
    return flavorList

def countInStock(flavors):
    count = 0
    for f in flavors:
        if f.upper() == 'VANILLA' or f.upper() == 'CHOCOLATE' or f.upper() == 'STRAWBERRY':
            count += 1
    return count
    
def main():
    flavs = getFlavors()
    c = countInStock(flavs)
    print 'We have %s of your flavors!' % c

main()