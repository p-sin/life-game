from setup import players
from setup.components import decks
from play.round import play_round

def __main__ ():
    #Add configuring of logic
    player_info, num_players = players.setup_players()
    game_space = players.GameSpace(player_info)

    for round in decks.keys():

        print (round)

        game_space = players.deal_cards(game_space, round, num_players)

        game_space = play_round(game_space, round, num_players)


    print (game_space)


if __name__ == '__main__':
    __main__ ()





# Loop through each player
# Select first card
# Select second card
# Play first card
# Play second card