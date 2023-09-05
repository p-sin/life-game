from life_game.play.game import Game
from life_game.play.players import create_players
from life_game.setup.deal import deal_cards, deal_events
from life_game.setup.setup_exceptions import (
    InvalidPlayerCountRange,
    InvalidPlayerCountType,
)


def valid_players(total_players: int) -> bool:
    if not isinstance(total_players, int):
        raise InvalidPlayerCountType(total_players)
    elif not 0 < total_players < 7:
        raise InvalidPlayerCountRange(total_players)
    else:
        return True


def __main__() -> None:
    total_players = 6

    for _ in range(10000):
        if valid_players(total_players):
            deals = deal_cards(total_players)
            players = create_players(total_players, deals)
            events = deal_events()
            game = Game(total_players, players, events)
            game.play_game()
        else:
            pass


if __name__ == "__main__":
    __main__()
