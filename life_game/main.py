from life_game.play.game import Game
from life_game.setup.cards import Cards
from life_game.setup.events import Events
from life_game.setup.players import Players
from life_game.util import valid_players


def __main__() -> None:
    total_players = 6
    valid_players(total_players)

    for _ in range(1):
        cards = Cards()
        events = Events()
        players = Players(total_players)
        game = Game(total_players, players, cards, events)
        game.play_game()


if __name__ == "__main__":
    __main__()
