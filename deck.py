import random
import cardsuit as cs
import cardvalues as value
import card



class Deck:

    numdecks = 1
    deck = []

    def __init__(self, numdecks=1):
        self.numdecks = numdecks
        self.initializeDeck()

    def initializeDeck(self):
        for num in range(0, self.numdecks):

            for num1 in range(1, 14):
                a = card.Card(num1, cs.CardSuit.SPADES)
                self.deck.append(a)

            for num1 in range(1, 14):
                a = card.Card(num1, cs.CardSuit.CLUBS)
                self.deck.append(a)

            for num1 in range(1, 14):
                a = card.Card(num1, cs.CardSuit.HEARTS)
                self.deck.append(a)

            for num1 in range(1, 14):
                a = card.Card(num1, cs.CardSuit.DIAMONDS)
                self.deck.append(a)

    def getCardArray(self):
        return self.deck

    def shuffleDeck(self, numshuffles=1):
        for num in range(0, numshuffles):
            #random.shuffle(self.deck)
            return

    def getNumDecks(self):
        return self.numdecks

    def fuckUpTheDeck(self): #creates an unfair deck for debugging purposes
        self.shuffleDeck()
        self.deck[12] = self.deck[28]
        self.deck[14] = self.deck[38]

    def getNumCards(self):
        return self.numdecks * 52

    def validateDeck(self): #checks for duplicate cards and returns true or false. True = deck is good
        for num in range(0, self.getNumCards()):
            v = self.deck[num].value
            s = self.deck[num].suit
            d = self.numdecks
            templist = []
            for num1 in range(0, self.getNumCards()):
                if self.deck[num1].value == v and self.deck[num1].suit == s:
                    templist.append(self.deck[num1])
            counter = len(templist)
            if counter == d:
                pass
            else:
                print("Deck is Invalidated:")
                return False

        print("Deck is Validated")
        return True

    def printDeck(self): #DEBUG function that prints the whole deck
        for num in range(0, self.getNumCards()):
            print(str(value.CardValues(self.deck[num].value).name) + " of " + str(self.deck[num].suit.name) + " with point value of " + str(self.deck[num].points))


