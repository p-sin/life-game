import pytest

from life_game.setup.players import create_players

test_deals = {
    "child": [1, 5, 23, 27, 34, 35, 43, 48, 51],
    "adol": [63, 76, 79, 85, 89, 101, 111, 115, 120],
    "adult": [125, 132, 138, 144, 148, 153, 156, 167, 179],
}


def test_player_choose_cards_is_card() -> None:
    """Tests that the outputs are card objects"""
    deals = test_deals
    players = create_players(1, deals)

    chosen_cards = players[1].choose_cards("child")

    try:
        slot_number = chosen_cards[0]["card_slot_1"]["slot_number"]
        assert True
    except:
        assert False


@pytest.mark.parametrize(
    "round, card_range",
    [
        ("child", [1, 5, 23, 27, 34, 35, 43, 48, 51]),
        ("adol", [63, 76, 79, 85, 89, 101, 111, 115, 120]),
        ("adult", [125, 132, 138, 144, 148, 153, 156, 167, 179]),
        ("child", [1, 5, 23, 27, 34, 35, 43, 48, 51]),
        ("adol", [63, 76, 79, 85, 89, 101, 111, 115, 120]),
        ("adult", [125, 132, 138, 144, 148, 153, 156, 167, 179]),
        ("child", [1, 5, 23, 27, 34, 35, 43, 48, 51]),
        ("adol", [63, 76, 79, 85, 89, 101, 111, 115, 120]),
        ("adult", [125, 132, 138, 144, 148, 153, 156, 167, 179]),
        ("child", [1, 5, 23, 27, 34, 35, 43, 48, 51]),
        ("adol", [63, 76, 79, 85, 89, 101, 111, 115, 120]),
        ("adult", [125, 132, 138, 144, 148, 153, 156, 167, 179]),
        ("child", [1, 5, 23, 27, 34, 35, 43, 48, 51]),
        ("adol", [63, 76, 79, 85, 89, 101, 111, 115, 120]),
        ("adult", [125, 132, 138, 144, 148, 153, 156, 167, 179]),
    ],
)
def test_player_choose_cards_exist(round, card_range) -> None:
    """Test that the card objects chosen exist in the deal supplied to the function"""
    deals = test_deals
    players = create_players(1, deals)

    chosen_cards = players[1].choose_cards(round)

    for card in chosen_cards:
        assert card["number"] in card_range


def test_player_choose_cards_unique() -> None:
    """Test that the cards chosen are not the same"""
    deals = test_deals
    players = create_players(1, deals)

    unique = True

    for _ in range(200):
        chosen_cards = players[1].choose_cards("child")
        if chosen_cards[0]["number"] == chosen_cards[1]["number"]:
            unique = False

    assert unique == True
