from life_game.play.players import create_players
from life_game.setup.components import rounds

from life_game.play.game import Game
from life_game.setup.deal import deal_cards


def __main__():
    total_players = 2

    deals = deal_cards(total_players)
    players = create_players(total_players, deals)
    game = Game(players)

    for round in rounds:
        game.card_phase(round)


# print(game.players[1])


if __name__ == "__main__":
    __main__()


# Loop through each player
# Select first card
# Select second card
# Play first card
# Play second card
