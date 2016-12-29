import deck
import dealer
import hand

class Player:

    wanthit = bool
    playeridentifier = int
    hand = object

    def __init__(self, handobj, playeridentifier):
        self.wanthit = False
        self.hand = handobj
        self.playeridentifier = playeridentifier


    def wantHit(self):
        print("\n")
        inp = input("Hit Hand " + str(self.playeridentifier) + "? (Y/N)")
        if inp.lower() == 'y' or 'n':
            if inp.lower() == 'n':
                self.wanthit = False
                return False
            elif inp.lower() == 'y':
                self.wanthit = True
                return True
        else:
            print("Invalid Choice")
            self.wanthit()











