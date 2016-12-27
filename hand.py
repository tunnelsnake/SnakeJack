import cardvalues as cv
import card
import cardsuit as cs

class Hand:

    card1 = card
    card2 = card
    hit = []
    hand = []

    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def addHit(self, hit):
        self.hit.append(hit)

    def totalValue(self): #make sure to update object's point value if it's an ace and you want it to be 11
        total = 0
        self.hand = self.hit
        self.hand.append(self.card1)
        self.hand.append(self.card2)
        for num in range(0, len(self.hand)):
            total += self.hand[num]
        return total

    def printHand(self):
        print("**HAND**")
        print(cv.CardValues(self.card1.value).name + " of " + cs.CardSuit(self.card1.suit).name)
        print(cv.CardValues(self.card2.value).name + " of " + cs.CardSuit(self.card2.suit).name)

