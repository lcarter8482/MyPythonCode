import Epic

verseNum = ["first", "second", "third", "fourth"]
verses = []

#getting each verse from user and putting into list verses
for verse in verseNum:
    userVerses = Epic.userString("Enter the %s verse:" % verse)
    verses.append(userVerses)

chorus = Epic.userString("Enter the chorus:")
repeat = Epic.userInt("Enter the chorus repeat:")

fullChorus = (chorus + ' ') * repeat
lastChorus = fullChorus + chorus

#changing verses to uppercase
verses = [element.upper() for element in verses]

#changing chorus to lowercase
fullChorus = fullChorus.lower()
lastChorus = lastChorus.lower()

#inserting chorus into verses
verses.insert(1, fullChorus)
verses.insert(3, fullChorus)
verses.insert(5, fullChorus)
verses.insert(7, lastChorus)
verses.insert(8, '...one more time!...')

song = (verses) * 2
del song[17]

print song
print

#printing out each element in song & replacing "cookies"
for lyrics in song:
    lyrics = lyrics.replace("COOKIES", "_______")
    print lyrics