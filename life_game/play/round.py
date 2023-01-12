from life_game.setup.players import GameSpace
from life_game.play.actions import select_card, play_card


def deal_cards(game_space: GameSpace, round: str, num_players: list[int]) -> GameSpace:
    def select_player_cards(deal: list[int], player: int) -> dict[int, card_type]:
        start = 0 + (9 * (player - 1))
        end = 9 + (9 * (player - 1))
        player_deal = deal[start:end]

        player_cards = {}

        for num, card in enumerate(player_deal):
            player_cards[num + 1] = cards[card]

        return player_cards

    deal = random.sample(decks[round], len(num_players) * 9)

    for player in num_players:
        player_cards = select_player_cards(deal, player)

        game_space.player_info[player].hand = player_cards

    return game_space


def play_round(game_space: GameSpace, round: str, num_players: list[int]) -> GameSpace:
    for player in num_players:
        hand = game_space.player_info[player].hand
        board = game_space.player_info[player].board

        chosen_cards = select_card(hand)

        for card in chosen_cards:
            game_space.player_info[player].board = play_card(board, hand, card)
