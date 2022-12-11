from setup import game
from setup.components import decks

def __main__ ():
    #Add configuring of logic
    player_info, num_players = game.setup_players()
    game_space = game.GameSpace(player_info)

    for round in decks.keys():
        game_space = game.deal_cards(game_space, round, num_players)


if __name__ == '__main__':
    __main__ ()




