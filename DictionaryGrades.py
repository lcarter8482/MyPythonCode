d = {}
for line in open("DictionaryGrades.txt"):
    temp = line.split(":")
    name = temp[0].strip()
    grade = temp[1].strip()
    d[name] = grade
    
print "Enter a name:",
n = raw_input()

if n in d: 
    print d[n]

if n not in d:
    print "%s is not in the file" % n