from life_game.setup.players import setup_players, deal_cards, Player

def test_setup_player_count() -> None:
    player_info, num_players = setup_players(3)

    assert num_players == [1,2,3]

def test_setup_player_info_count() -> None:

    player_info, num_players = setup_players(2)

    assert list(player_info.keys()) == [1,2]

def test_setup_player_info_type() -> None:

    player_info, num_players = setup_players(1)

    assert isinstance(player_info[1], Player)
