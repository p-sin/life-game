from life_game.setup import players
from life_game.setup.components import rounds
from life_game.play.round import play_round, deal_cards


def __main__():
    # Add configuring of logic

    total_players = 2

    game_space, num_players = players.setup_players(total_players)

    for round in rounds:
        game_space = deal_cards(game_space, round, num_players)

        game_space = play_round(game_space, round, num_players)

    print(game_space)


if __name__ == "__main__":
    __main__()


# Loop through each player
# Select first card
# Select second card
# Play first card
# Play second card
