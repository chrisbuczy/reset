# golfDeck.py
# file for deck of cards for golf game
cardsCopy = ['a', 'a', 'a', 'a', 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9,
                9, 'j', 'j', 'j', 'j', 'q', 'q', 'q', 'q', 'k', 'k', 'k', 'k']


class fullDeck:

    # initialize deck and top card of discard pile
    def __init__(self):
        self.deckOfCards = ['a', 'a', 'a', 'a', 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9,
                9, 'j', 'j', 'j', 'j', 'q', 'q', 'q', 'q', 'k', 'k', 'k', 'k']
        self.topDiscard = 0
    

    # function used to print out actual deck when refered to
    def __str__(self) -> list:
        return(self.deckOfCards)
    

    # remove dealt cards from deck
    def removeCards(self, cards=list):
        for card in cards:
            self.deckOfCards.remove(card)






deck = fullDeck()