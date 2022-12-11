
from dataclasses import dataclass

hand = []
players = {}

@dataclass
class Player:
    hand: list[int]

@dataclass
class Game:
    players: dict[int, Player]

for x in range (1,4):
    players[x] = Player(hand)

game = Game(players)

cards = [1,2,3,4,5,6]

for x in range (1,4):

    start = 0 + (2 * (x - 1))
    end = 2 + (2 * (x - 1))

    card_nums = cards[start:end]


    game.players[x].hand = card_nums

print (game)
