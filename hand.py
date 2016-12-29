import cardvalues as cv
import card
import cardsuit as cs
import copy

class Hand:

    card1 = card
    card2 = card
    identifier = 0
    cardlist = list
    hits = list

    def __init__(self, card1, card2, identifier):
        self.card1 = card1
        self.card2 = card2
        self.identifier = identifier
        self.hits = []
        self.hand = []

    def addHit(self, card):
        self.hits.append(card)

    def totalPoints(self): #make this function autototal and do ace manipulation as well.
        total = 0
        aces = [] #this will store the position of aces in the cardlist array so if need be we can adjust their value
        containsace = False
        cardlist = copy.copy(self.hits)
        cardlist.append(self.card1)
        cardlist.append(self.card2)
        if self.card1.value == 1:  #check to see if we have a blackjack between the first two cards first
            for num in range(0, len(cardlist)): #we don't use containsace because this checks strictly for s blackjack
                total += cardlist[num].points
                if total == 21:
                    return 21
        if self.card2.value == 1: #ditto ^^
                total = 0 #reset total value
                for num in range(0, len(cardlist)):
                    total += cardlist[num].points
                    if total == 21:
                        return 21
        for num in range(0, len(cardlist)):
            if cardlist[num].value == 1: #This whole section sets ace reference numbers and containsace if there are aces
                aces.append(num)
        if len(aces) == 0:
            containsace = False
        else:
            containsace = True
        if containsace == False:  #This checks for a hand with no aces, and if there arent any, just return the total.
            total = 0 #reset total value
            for num in range(0, len(cardlist)):
                total += cardlist[num].points
            return total
        else: #Here is where the logic for if the hand contains aces are
            indexcounter = 0
            total = 0
            for num in range(0, len(cardlist)): #get the total value
                total += cardlist[num].points
            if total > 21:
                total = 0
                for num in range(0, len(aces)): #if the total is greater than 21 then set each ace to low value until its under 21
                    total = 0 #reset total for every iteration
                    for num1 in range(0, len(cardlist)):  # get the new total value each iteration
                        total += cardlist[num1].points
                    if total < 21:
                        return total
                    a = aces[num]
                    cardlist[a].assignPointValue(False)
                total = 0
                for num1 in range(0, len(cardlist)):  # get the new total value each iteration
                    total += cardlist[num1].points
            else:
                return total
        total = 0
        for num in range(0, len(cardlist)):
            total += cardlist[num].points
        return total

    def printHand(self):
        print("Hand With Identifier " + str(self.identifier))
        print(cv.CardValues(self.card1.value).name + " of " + cs.CardSuit(self.card1.suit).name)
        print(cv.CardValues(self.card2.value).name + " of " + cs.CardSuit(self.card2.suit).name)
        for num in range(0, len(self.hits)):
            print(str(cv.CardValues(self.hits[num].value).name) + " of " + cs.CardSuit(self.hits[num].suit).name)
        print("Total Value: " + str(self.totalPoints()))
        print("\n")

    def printIdentifier(self):
        print(str(self.identifier))
