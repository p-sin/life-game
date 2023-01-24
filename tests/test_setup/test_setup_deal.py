import pytest

from life_game.setup.deal import deal_cards, deal_events
from life_game.setup.attr_cards import cards


@pytest.mark.parametrize("round", [("child"), ("adol"), ("adult")])
def test_deal_correct_rounds(round):
    """Test that the deal function generates a deal for each round"""
    deals = deal_cards(6)
    assert round in deals


@pytest.mark.parametrize(
    "round, total_players, num_cards",
    [
        ("child", 1, 9),
        ("adol", 1, 9),
        ("adult", 1, 9),
        ("child", 2, 18),
        ("adol", 2, 18),
        ("adult", 2, 18),
        ("child", 3, 27),
        ("adol", 3, 27),
        ("adult", 3, 27),
        ("child", 4, 36),
        ("adol", 4, 36),
        ("adult", 4, 36),
        ("child", 5, 45),
        ("adol", 5, 45),
        ("adult", 5, 45),
        ("child", 6, 54),
        ("adol", 6, 54),
        ("adult", 6, 54),
    ],
)
def test_deal_correct_num_cards(round, total_players, num_cards):
    """Test that the deal function generates the correct number of card numbers
    for the player count"""
    deals = deal_cards(total_players)
    assert len(deals[round]) == num_cards


@pytest.mark.parametrize("round", [("child"), ("adol"), ("adult")])
def test_deal_cards_from_correct_round(round) -> None:
    """Tests that all the cards in the deal are from the correct round"""
    for x in range(100):
        deals = deal_cards(1)
        deal = deals[round]
        for card in deal:
            assert cards[card]["board_section"].value.life_stage == round


@pytest.mark.parametrize("round", [("child"), ("adol"), ("adult")])
def test_event_deal_correct_rounds(round):
    """Test that the event deal function generates a deal for each round"""
    event_deals = deal_events()
    assert round in event_deals


@pytest.mark.parametrize("round", [("child"), ("adol"), ("adult")])
def test_event_deal_correct_num_cards(round) -> None:
    """Test that each round's event deal has the correct number of cards in it"""
    event_deals = deal_events()
    assert len(event_deals[round]) == 5


@pytest.mark.parametrize("round", [("child"), ("adol"), ("adult")])
def test_deal_event_cards_from_correct_round(round) -> None:
    """Tests that all the cards in the event deal are from the correct round"""
    for x in range(100):
        event_deals = deal_events()
        deal = event_deals[round]
        for _, event in deal.items():
            assert event["life_stage"] == round


@pytest.mark.parametrize("round", [("child"), ("adol"), ("adult")])
def test_deal_event_cards_duplicates(round) -> None:
    """Tests that all the cards in the event deal are unique"""
    for x in range(100):
        event_deals = deal_events()
        deal = event_deals[round]
        cards = set([x for x in deal.keys()])
        assert len(cards) == 5
