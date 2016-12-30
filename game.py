import dealer
import deck
import player
import card
import hand
import cardvalues as cv
import cardsuit as cs


#TODO:
#Line 31, 36, 43 of hand, change 1 to corresponding enumeration of value

class Game:
    numplayers = int
    players = list
    dealer = object
    dealerplayer = object
    hands = list

    def __init__(self, numplayers):
        self.numplayers = numplayers
        gd = deck.Deck(1)
        cards = gd.getCardArray()
        gd.shuffleDeck()
        d = dealer.Dealer(cards, numplayers)
        self.dealer = d
        d.deal()
        self.hands = d.getHandArray()
        d.printAllHands()
        self.createPlayers() #this function doesn't return anything. Remember that.
        self.startGameLogic()

    def createPlayers(self):  # the number of elements in 'hands' determines the number of player objects
        numplayers = len(self.hands) - 1  # subtract 1 to exclude the dealer's hand. The dealer's hand is set in the dealer class
        players = []
        for num in range(0, numplayers):
            x = self.hands[num].identifier
            a = self.hands[num]
            b = player.Player(a, x)
            players.append(b)
        self.dealerplayer = player.Player(self.hands[len(self.hands) - 1], self.dealer.dealeridentifier) #this will always return the very last hand in the hands list which is always the dealer
        self.players = players

    def startGameLogic(self):
        for num in range(len(self.players)):
            self.askHit(self.players[num].playeridentifier)
        self.askDealerHit()
        print("\n")
        print("Players and Dealer Done taking hits. Checking Cards.")
        print("\n")
        self.dealer.printAllHands(True)
        print("Total Value: " + str(self.hands[self.dealer.dealeridentifier].totalPoints()))

    def askHit(self, playeridentifier):
        while True:
            if self.players[playeridentifier].hand.totalPoints() > 21:
                print('Cannot Hit. Player with identifier ' + str(
                    self.players[playeridentifier].playeridentifier) + " is bust with a value of " + str(
                    self.players[playeridentifier].hand.totalPoints()))
                break
            var = self.players[playeridentifier].wantHit()
            if var == True and self.players[playeridentifier].hand.totalPoints() != 21:
                print("Player with identifier " + str(self.players[playeridentifier].playeridentifier) + " is hitting. Now has hand: \n")
                self.dealer.hit(self.players[playeridentifier].playeridentifier)
                self.players[playeridentifier].hand.printHand()
            else:
                print("Player with identifier " + str(self.players[playeridentifier].playeridentifier) + " is staying. Now has hand: \n")
                self.players[playeridentifier].hand.printHand()
                break

    def askDealerHit(self): #This is an attempt at basic dealer AI.
        while True:
            if self.dealerplayer.hand.totalPoints() >= 17:
                print("Dealer with identifier " + str(self.dealerplayer.playeridentifier) + " is staying. Now has hand: \n")
                self.dealer.printDealerHand()
                break
            else:
                self.dealer.hit(self.dealerplayer.playeridentifier)
                print("Dealer with identifier " + str(self.dealerplayer.playeridentifier) + " is hitting. Now has hand: \n")
                self.dealer.printDealerHand()





Game(2)
