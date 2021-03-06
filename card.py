import cardsuit as cs
import cardvalues as values

class Card:
    value = 0
    suit = 0
    points = 0

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.assignPointValue()

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    def setSuit(self, suit):
        self.suit = suit

    def setValue(self, value):
        self.value = value

    def assignPointValue(self, highaceval=True):
        pv = self.value

        if pv in range(10, 14): #check to see if the card is a face card or 10
            self.points = 10

        if pv < 10:  #check to see the value, if less that 10, then equals specified number
            self.points = pv


        if pv == 1 and highaceval == False:  #protection against misuse of function for assigning 11 to other card values
            self.points = 1

        if pv == 1 and highaceval == True:
            self.points = 11

    def printAttributes(self):
        print(values.CardValues(self.value).name + " of " + cs.CardSuit(self.suit).name + " with a point value of " + str(self.points))
