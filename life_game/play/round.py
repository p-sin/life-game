from setup.players import GameSpace
from play.actions import select_card, play_card


def play_round(game_space: GameSpace, round: str, num_players: list[int]) -> GameSpace:

    for player in num_players:

        hand = game_space.player_info[player].hand
        board = game_space.player_info[player].board

        chosen_cards = select_card(hand)

        for card in chosen_cards:

            game_space.player_info[player].board = play_card(board, hand, card)



  