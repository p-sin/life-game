from life_game.setup.boards import Board


num_players = 4
num_players_var = num_players + 1


for player in range(1, num_players_var):
    board = Board()
    hand = Hand()
    