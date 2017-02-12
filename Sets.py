def containsNoCase(item, l):
    yes = False
    for index in l:
        if item.upper() == index.upper():
            yes = True
            break
    return yes


def intersection(set1, set2):
    result = []
    for i in set1:
        if containsNoCase(i, set2):
            result.append(i)
    return result


def union(set1, set2):
    result = []
    for i1 in set1:
        if not containsNoCase(i1, result):
            result.append(i1)
    
    for i2 in set2:
        if not containsNoCase(i2, result):
            result.append(i2)
    return result


def readStudents(filename):
    file = open(filename)
    l = []
    for item in file:
        l.append(item.strip())
    return l

def main():
    calc = readStudents('calc-students.txt')
    phys = readStudents('physics-students.txt')
    bothClasses = intersection(calc, phys)
    eitherClass = union(calc, phys)
    
    print '%s students are in both classes' % bothClasses
    print '%s students are in either class' % eitherClass
    
    
main()
    