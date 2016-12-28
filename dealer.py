import hand

class Dealer:
    numplayers = int
    hands = []
    cards = []
    cardcounter = 0;

    def __init__(self, cards, numplayers): #numplayers is not including the dealer
        self.numplayers = numplayers
        self.cards = cards

    def deal(self):
        self.counter = 0 #Create players hands
        for num in range(0, self.numplayers):
            for num1 in range(0, 2):
                a = hand.Hand(self.cards[self.counter], self.cards[self.counter + 1])
                self.hands.append(a)
                self.counter +=2

            #create dealer's hand
            a = hand.Hand(self.cards[self.counter], self.cards[self.counter + 1])
            self.hands.append(a)
            self.counter += 2

        return self.hands