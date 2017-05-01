import Epic

suspects = ['Miss Scarlet', 'Col Mustard', 'Mr Green']
weapons = ['Candlestick', 'Wrench', 'Pipe']
p = []

for suspect in suspects:
    for weapon in weapons:
        p.append('%s with the %s' % (suspect, weapon))

while len(p) > 1:
    print "%s possibilities left " % len(p)
    possibilites = Epic.userString("Is the clue about a suspect (s) or a weapon (w)?")    

    if possibilites == "w":
        w = Epic.userString("Enter the weapon that was not used (%s):" % weapons)
        w = w.upper()
        for i in range(len(p)):
            if w in p[i].upper():
                p[i] = "" #replaces the specific place with a blank spot
    for i in p:
        if i == "":
            p.remove(i) #removes blank spot

    if possibilites == "s":
        s = Epic.userString("Enter the innocent suspect (%s):" % suspects)
        s = s.upper()
        for i in range(len(p)):
            if s in p[i].upper():
                p[i] = "" #replaces the specific place with a blank spot
                
    for i in p:
        if i == "":
            p.remove(i) #removes blank spot
            
print "\nIt must have been %s" % p