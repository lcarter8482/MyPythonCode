import os
import Epic

files = os.listdir(".")
txtFiles = []

def main():
    userWord = Epic.userString("Enter A Search Word: ")
    openFiles()
    counter = search(files, userWord)
    print "\nWord Found %s times" % counter

#opens all files ending in .txt in current directory
def openFiles():
    for file in files:
        if file.endswith(".txt"):
            txtFiles.append(file)
    return

#reads in data from files and searches for user's word        
def search(file, userWord):
    count = 0
    for f in txtFiles:
        allFiles = open(f)
        data = allFiles.read()
        data = data.split("\n")
        for l in data:
            if userWord.upper() in l.upper():
                print "%s: %s" % (f, l.upper().strip())
                count = count + 1
    return count
    #returns how many times the word was found

main()