import os
import Epic

files = os.listdir(".")
txtFiles = []
count = 0

userWord = Epic.userString("Enter word: ")

allFiles = []
for file in os.listdir("."):
    if file.endswith(".txt"):
        f = open(file)
        for item in f:
         allFiles.append(item)

for line in allFiles:
    if userWord.upper() in line.upper(): 
        count = count + 1
        print line.upper().strip()
        print os.path.basename(file)
print count

#os.path.join(file)

#for file in files:
 #   if file.endswith(".txt"):
  #      f = open(file)
   #     txtFiles.append(f)

#for line in txtFiles:
 #   if userWord in line: 
  #      print line.upper()
        
#for file in files:
 #   if file.endswith(".txt"):
  #      f = open(file, 'r')
        