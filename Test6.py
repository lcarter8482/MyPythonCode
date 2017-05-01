import Epic

suspects = ['Miss Scarlet', 'Col Mustard', 'Mr Green']
weapons = ['Candlestick', 'Wrench', 'Pipe']
p = []

def poss():
    suspects = ['Miss Scarlet', 'Col Mustard', 'Mr Green']
    weapons = ['Candlestick', 'Wrench', 'Pipe']
    for suspect in suspects:
        for weapon in weapons:
            p.append('%s with the %s' % (suspect, weapon))
    return p
    
def searchW(w):
    if possibilites == w:
        w = Epic.userString("Enter the weapon that was not used (%s):" % weapons)
        w = w.upper()
        for i in range(len(p)):
            if w in p[i].upper():
                p[i] = "" #replaces the specific place with a blank spot
    for i in p:
        if i == "":
            p.remove(i) #removes blank spot
    return p
def searchS(s):
    if possibilites == s:
        s = s.upper()
        for i in range(len(p)):
            if s in p[i].upper():
                p[i] = "" #replaces the specific place with a blank spot
                
    for i in p:
        if i == "":
            p.remove(i) #removes blank spot
    return p
            
            
def main():
    p = poss()
    w = Epic.userString("Enter the weapon that was not used (%s):" % weapons)
    weapon = searchW(w)
    s = Epic.userString("Enter the innocent suspect (%s):" % suspects)
    suspect = searchS(s)
    while len(p) > 1:
        print "%s possibilities left " % len(p)
        possibilites = Epic.userString("Is the clue about a suspect (s) or a weapon (w)?")   
    print "\nIt must have been %s" % p