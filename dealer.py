import hand

class Dealer:
    numplayers = int
    hands = list
    cards = list
    cardcounter = 0;
    dealeridentifier = int

    def __init__(self, cards, numplayers): #numplayers is not including the dealer
        self.hands = []
        self.cards = []
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

    def hit(self, playeridentifier):
        self.hands[playeridentifier].addHit(self.cards[self.counter])
        self.counter += 1

    def getHandArray(self):
        return self.hands

    def printAllHands(self, showdealerholecard = False):
        for num in range(0, self.numplayers):
            self.hands[num].printHand()
        self.printDealerHand(showdealerholecard)

    def printDealerHand(self, showholecard = False):
        print("Dealer Hand With Identifier " + str(self.dealeridentifier))
        x = self.hands[len(self.hands) - 1]
        x.card1.printAttributes()
        if showholecard == False:
            print("HOLE CARD")
        else:
            x.card2.printAttributes()
        for num in range(0, len(x.hits)):
            x.hits[num].printAttributes()
            print("\n")



