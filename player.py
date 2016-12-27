import deck
import hand

d = deck.Deck(1)
cards = d.initializeDeck()
d.validateDeck()
d.shuffleDeck(3)
h = hand.Hand(cards[0], cards[1])
h.printHand()


