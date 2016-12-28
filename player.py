import deck
import hand
import dealer
import card

#TODO:
#redo fisher-yates shuffle
#clean up functions
#work up to hit system
#systematic play
#numerical players and order
#expand deck validation


gamedeck = deck.Deck(1)
gamedeck.shuffleDeck()
gamedeck.printDeck()
gamedeck.validateDeck()
cards = gamedeck.getCardArray()
cards[51].printAttributes()






