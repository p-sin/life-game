SETUP TESTS

1) Check that all expected attributes have been defined
2) Check that all board sections have been defined
3) Check all attribute slots have been defined with empty values
4) Check the Board class is generated correctly
5) Check that each deck contains the expected card IDs

CARD TESTS
1) Check the correct number of cards are defined
2) Check each board section has the correct number of cards assigned to it
3) Check each card slot contains attribute slots that belong in that card slot
4) Check each card slot fulls its values from the same board_setion as defined in the card
5) Check that the total pool of cards contain the correct total value of attribute values

PLAYER TESTS
1) Check that setup_players returns a correct list of players
2) Check that setup_player exceptions trigger for number of players
