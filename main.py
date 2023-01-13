from life_game.setup.players import create_players
from life_game.setup.components import rounds

# from life_game.play.game_space import Game
from life_game.setup.deal import deal_cards


def __main__():
    total_players = 2

    deals = deal_cards(total_players)
    players = create_players(total_players, deals)

    game = Game(players)

    for round in rounds:
        game.play_round(round)

        game_space = play_round(game_space, round, num_players)

    print(game_space)


if __name__ == "__main__":
    __main__()


# Loop through each player
# Select first card
# Select second card
# Play first card
# Play second card
