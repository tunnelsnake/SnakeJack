import card
import cardpoints
import cardsuit
import cardvalues
import dealer
import deck
import hand
import player



class Game():
    numplayers = int
    players = list
    dealer = object
    hands = list

    def __init__(self, numplayers):
        self.numplayers = numplayers
        gd = deck.Deck(1)
        cards = gd.getCardArray()
        d = dealer.Dealer(cards, numplayers)
        self.dealer = d
        d.deal()
        self.hands = d.getHandArray()
        d.printPlayerhands()
        players = self.createPlayers()
        self.startGameLogic()

    def createPlayers(self): #the number of elements in 'hands' determines the number of player objects
        numplayers = len(self.hands) - 1 #subtract 1 to exclude the dealer's hand. The dealer's hand is set in the dealer class
        players = []
        for num in range(0, numplayers):
            x = self.hands[num].identifier
            a = self.hands[num]
            b = player.Player(a, x)
            players.append(b)
        self.players = players


    def startGameLogic(self):
        for num in range(len(self.players)):
            a = self.players[num]
            var = a.wantHit()
            if var == True:
                print("Player with identifier " + str(a.playeridentifier) + " is hitting. Now has hand: \n")
                self.dealer.hit(self.players[num].playeridentifier)
                self.players[num].hand.printHand()
            else:
                print("Player with identifier " + str(a.playeridentifier) + " is staying with hand: \n")
                self.players[num].hand.printHand()
        for num in range(len(self.players)):
            a = self.players[num]
            a.hand.printHand()




Game(4)



