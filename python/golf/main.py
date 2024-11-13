# main.py
# main golf game
import golfDeck
import players
round = 1


for instance in players.player.instanceList:  
    nestRound = 0
    print("new")
    while nestRound != 4:
        instance.play()
        nestRound += 1
        print(nestRound)

for instance in players.player.instanceList:
    print(instance)

print(golfDeck.deck.deckOfCards)
