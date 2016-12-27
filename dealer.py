import card
import cardpoints
import cardsuit
import cardvalues
import deck
import hand


class Dealer:
    numplayers = int
    hands = []
    d = deck.Deck(4)
    cards = d.initializeDeck()
    d.validateDeck()
    d.shuffleDeck()

    def __init__(self, numplayers): #numplayers is not including the dealer
        self.numplayers = numplayers

    def deal(self):
        counter = 0
        #for num in range(0, self.numplayers * 2):
            #a =