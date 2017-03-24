import random

rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

#building the deck from each rank to each suit
def buildDeck(rank, suit):
    deck = ["%s of %s" % (r, s) for r in rank for s in suit]
    return deck

#randomly shuffles the deck
def shuffle(deck):
    random.shuffle(deck)
    return deck

#takes only the first 5 cards out of the list
def deal(deck):
    dealDeck = deck[:5]
    return dealDeck

def main():
    deck = buildDeck(rank, suit)
    print "Your delt hand:",
    deck = shuffle(deck)    
    deck = deal(deck)
    
    print deck

main()