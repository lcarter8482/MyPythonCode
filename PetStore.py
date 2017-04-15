import Epic
import json

def main():
    searchType = Epic.userString("Search by category (c) or keyword (k)? ")
    if searchType == "k":
        keyword = Epic.userString("Enter a keyword: ")
        search(keyword.upper()) #will run search function looking for keyword
    elif searchType == "c":
        category = Epic.userString("Enter a category: ")
        search(category.upper()) #will run search function looking for category

#reads in a file & returns String    
def getJson(filename):
    jsonTxt = ""
    f = open(filename)
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    petSupplies = json.loads(jsonTxt)
    return petSupplies
    
#search function that reads through the name searched and prints specified items    
def search(supplyType):
    supplies = getJson("PetStore.json") #using the function to read in json file
    for stuff in supplies:
        if stuff["Category"].upper() == supplyType: #searching through categories for desired supply type
            print "%s - %s" % (stuff["Product"], stuff["Price"])
        elif supplyType in stuff["Product"].upper(): #searching through product names for keyword entered
            print "%s - %s" % (stuff["Product"], stuff["Price"])
    return

main()