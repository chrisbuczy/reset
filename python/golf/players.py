# players.py
# file for player object
import golfDeck
import random

class player:

    #list of players
    instanceList = []


    # initalize hand and remove cards from deck that are in hand
    def __init__(self, name=None) -> None:

        self.instanceList.append(self)

        # initialize other stuff
        self.realHand = random.choices(golfDeck.deck.deckOfCards, k = 4)
        golfDeck.deck.removeCards(self.realHand)
        self.shownHand = ['?', '?', '?', '?']
        self.score = 0
        self.name = name
        self.nestRound = 0
    
    
    # function used to print out stats of player when refered to
    def __str__(self) -> str:
        return f'{self.name} {self.shownHand}'
    

    # main game function
    def play(self) -> None:

        # drawn card
        self.draw = [random.choice(golfDeck.deck.deckOfCards)]
        golfDeck.deck.removeCards(self.draw)

        # reveal card
        self.shownHand[self.nestRound] = self.realHand[0]
        print(self.shownHand)
        self.swapOrDiscard = input(f"you drew a ({self.draw}), Would you like to swap or discard the card (s or d): ")
        if self.swapOrDiscard == 's':
             print(self.whatSwap())
       

    # function to figure out what card to swap and swap it
    def whatSwap(self) -> list:
       
       # swap out card
        self.whichCard = int(input("Which card would you like to swap out (1, 2, 3, or 4): "))
        try:
            self.realHand[self.whichCard - 1] = self.draw
            self.shownHand[self.whichCard - 1] = self.draw
        except IndexError:
            self.whatSwap()
        
        return self.shownHand
            





# test area
player1 = player("Christian")
player2 = player("Mama")
print(player1.realHand, player2.realHand)
print(golfDeck.deck.deckOfCards)