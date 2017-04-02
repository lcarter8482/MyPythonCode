import Epic

def getFile(filename):
    file = open(filename)
    allFile = []
    for line in file:
        allFile.append(line)
    return allFile

def wordSearch(file,userWord):
    for line in file:
        if userWord.upper() in line.upper(): 
            print line.upper().strip()
    return
    
def main():
    searchWord = Epic.userString('Enter A Search Term: ')

    file = getFile('recipes.txt')
    file1 = getFile('bread.txt')
    file2 = getFile('firstAid.txt')
    file3 = getFile('trivia.txt')
    wordSearch(file,searchWord)
    wordSearch(file1,searchWord)
    wordSearch(file2,searchWord)
    wordSearch(file3,searchWord)

main()