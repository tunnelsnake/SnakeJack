import hand

class Dealer:
    numplayers = int
    hands = []
    cards = []
    cardcounter = 0;
    dealeridentifier = int

    def __init__(self, cards, numplayers): #numplayers is not including the dealer
        self.numplayers = numplayers
        self.cards = cards

    def deal(self):
        self.counter = 0 #Create players hands
        for num in range(0, self.numplayers):
            a = hand.Hand(self.cards[self.counter], self.cards[self.counter + 1], int(self.counter / 2 ))
            self.hands.append(a)
            self.counter +=2

        #create dealer's hand
        self.dealeridentifier = len(self.hands)
        a = hand.Hand(self.cards[self.counter], self.cards[self.counter + 1], self.dealeridentifier)
        self.hands.append(a)
        self.counter += 2

    def hit(self, playeridentifier): #This function is not the problem, we bypass it completely in player.py using the hand object's addHit method
        self.hands[playeridentifier].addHit(self.cards[self.counter])
        self.counter += 1

    def getHandArray(self):
        return self.hands