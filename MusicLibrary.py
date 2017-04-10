import json
import Epic

def main():
    artistName = Epic.userString("Enter An Artist Name: ")
    search(artistName)

#reads in a file & returns String    
def getJson(filename):
    jsonTxt = ""
    f = open(filename)
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    library = json.loads(jsonTxt)
    return library

#search function that reads through the name searched and prints specified items    
def search(name):
    albums = []
    years = []
    library = getJson("MusicLibrary.json") #using the function to read in json file
    for artist in library:
        if artist["Artist"] == name:
            for album in artist["Albums"]:
                albums.append(album) #list of all albums for each artist
            for year in artist["Year"]:
                years.append(year) #list of all years for each artist
    for i in range(len(albums)):
        print "%s: %s" % (albums[i], years[i])
    return

main()