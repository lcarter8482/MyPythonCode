import json
import Epic

def main():
    artistName = Epic.userString("Enter An Artist Name: ")
    search(artistName)
    
def getJson(filename):
    jsonTxt = ""
    f = open(filename)
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    library = json.loads(jsonTxt)
    return library
    
def search(name):
    albums = []
    years = []
    library = getJson("MusicLibrary.json")
    for artist in library:
        if artist["Artist"] == name:
            for album in artist["Albums"]:
                albums.append(album)
            for year in artist["Year"]:
                years.append(year)
    for i in range(len(albums)):
        print "%s: %s" % (albums[i], years[i])
    return

main()