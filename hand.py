import cardvalues as cv
import card
import cardsuit as cs

class Hand:

    card1 = card
    card2 = card
    identifier = 0
    hand = list
    hits = list

    def __init__(self, card1, card2, identifier):
        self.card1 = card1
        self.card2 = card2
        self.identifier = identifier
        self.hits = []
        self. hand = []

    def addHit(self, card):
        print("Hit Appended")
        self.hits.append(card)

    def totalPoints(self): #make sure to update object's point value if it's an ace and you want it to be 11
        total = 0
        list = self.hits
        list.append(self.card1)
        list.append(self.card2)
        for num in range(0, len(self.hand) + len(self.hits)):
            total += list[num].points
        return total

    def printHand(self):
        print("Hand With Identifier " + str(self.identifier))
        print(cv.CardValues(self.card1.value).name + " of " + cs.CardSuit(self.card1.suit).name)
        print(cv.CardValues(self.card2.value).name + " of " + cs.CardSuit(self.card2.suit).name)
        for num in range(0, len(self.hits)):
            print(str(cv.CardValues(self.hits[num].value).name) + " of " + cs.CardSuit(self.hits[num].suit).name)
        print("\n")

    def printIdentifier(self):
        print(str(self.identifier))
