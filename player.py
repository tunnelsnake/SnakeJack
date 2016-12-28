import deck
import dealer
import card

gamedeck = deck.Deck(1)
#gamedeck.shuffleDeck() #shuffling is turned of to make it easier to diagnose
#gamedeck.printDeck()   #enable to print the deck one card at a time
gamedeck.validateDeck() #makes sure there are no duplicate cards
cards = gamedeck.getCardArray() #returns the 'deck' of cards for local manipulation
d = dealer.Dealer(cards, 4) #pass 'deck' and number of players (dealer not included)
d.deal()
hands = d.getHandArray() #returns dealt hand objects with unique identifiers
hands[1].addHit(card.Card(1, 1)) #hits with the ace of spades for easier debug


for num in range(0, len(hands)):
    hands[num].printHand()
    print("\n")

print("Dealer Has Identifier " + str(d.dealeridentifier))
print(len(hands[2].hits))










