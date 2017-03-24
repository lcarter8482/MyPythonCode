import Epic

rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

#building the deck from each rank to each suit
def buildDeck(rank, suit):
    deck = ["%s of %s" % (r, s) for r in rank for s in suit]
    return deck

def shuffle(deck):
    #splitting the deck in half
    half1 = deck[:26]
    half2 = deck[26:]
    
    #interleaving each element in the lists
    for i in range(0,26):
        deck[2*i] = half1[i]
        deck[2*i+1] = half2[i]
    return deck

#takes only the first 5 cards out of the list
def deal(deck):
    dealDeck = deck[:5]
    return dealDeck

def main():
    deck = buildDeck(rank, suit)
    number = Epic.userInt("How many times do you want me to shuffle? ")
    
    #shuffles the deck the amount of times chosen by the user
    for i in range(0, number):
        deck = shuffle(deck)
        
    deck = deal(deck)
    
    print deck

main()