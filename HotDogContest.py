import Epic
import random
import time

#gets user input of winner
def userInput():
    guess = Epic.userString("Pick a winner (Tom, Sally, or Fred): ")
    return guess.lower()

#user places bet (bet has to be less than cash on hand)
def placeBet(cash):
    bet = Epic.userInt("How much would do you want to bet? (cash: $%s) " % cash)
    
    while bet > cash:
        print "You don't have that much money!"
        bet = Epic.userInt("How much would do you want to bet? (cash: $%s) " % cash)
    
    return bet

#gets random number    
def getRandomNum():
    num = random.randrange(1, 6)
    return num

#finds the winner based on who has highest number of hotdogs    
def findWinner(contestants):
    keys = list(contestants)
    maxKey = keys[0]
    maxValue = contestants[maxKey]
    
    for x in contestants.keys():

        if contestants[x] > maxValue:
            maxKey = x
            maxValue = contestants[x]
    
    return maxKey
    
def main():
    
    cash = 100
    
    while cash > 0:
        tom = 0
        sally = 0
        fred = 0
        
        guess = userInput()
        bet = placeBet(cash)
        
        print "Ready..."
        time.sleep(1)
        print "Set..."
        time.sleep(1)
        print "Eat!"
        #continues until someone gets to 50
        while tom < 50 and sally < 50 and fred < 50:
            tom += getRandomNum()
            sally += getRandomNum()
            fred += getRandomNum()
            
            print "\nTom has eaten %s hotdogs!" % tom
            print "Sally has eaten %s hotdogs!" % sally
            print "Fred has eaten %s hotdogs!" % fred
            print "\nchomp... chomp... chomp"
            time.sleep(1)
            
        contestants = {"tom" : tom, "sally" : sally, "fred" : fred}
        winner = findWinner(contestants)
        #finds if guess and actual winner are equal
        if guess == winner:
            cash += bet
            print "You guessed right! %s won!" % winner.title()
        else:
            cash -= bet
            print "Sorry, %s didn't win. %s won." % (guess.title(), winner.title())
        
        print "You have $%s" % cash
    
main()