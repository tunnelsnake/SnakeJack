import cardvalues as value
import cardsuit as cs
import card
import deck


# for num1 in range(1, 14):
#     a = card.Card(num1, cs.CardSuit.SPADES)
#     cards.append(a)
#
#
# for num1 in range(1, 14):
#     a = card.Card(num1, cs.CardSuit.CLUBS)
#     cards.append(a)
#
#
# for num1 in range(1, 14):
#     a = card.Card(num1, cs.CardSuit.HEARTS)
#     cards.append(a)
#
#
# for num1 in range(1, 14):
#     a = card.Card(num1, cs.CardSuit.DIAMONDS)
#     cards.append(a)

d = deck.Deck(2)
cards = d.initializeDeck()
d.fuckUpTheDeck()
if d.validateDeck() == True:
    print("Deck is Validated.")
else:
    print("Deck is Invalid")

for num in range(0, d.getNumCards()):
    ps = cards[num]
    ps.assignPointValue(True)
    print(str(value.CardValues(ps.value).name) + " of " + str(ps.suit.name) + " with point value of " + str(ps.points))
