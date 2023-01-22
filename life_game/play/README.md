1) players.py

Contains the definition, methods and supplemental functions for the player class

A player consists of:
- A board (Board object, as defined in components.py) which stores all the information about the cards played by the player
- A child, adol and adult hand which is derived from the deal cards and is where the integer based deck/deal values are converted to the actual card objects
- A logic module for driving the AI

create_players, select_player_cards and select_player_deal are functions called during the setup of the game to create and define individual players. These are passed into a 'players' dictionary which is passed into the Game. From here the Game is able to access each player and call the methods attached to each player object.

- create_players: Generates a Board, child/adol/adult hand and logic and instantiates a Player object with those values
- select_player_cards: Creates a hand object for each round by selecting x:y cards from the dealt card integers. This is defined by the player number, ensuring that each player takes the 'next' slice of cards from the dealt cards. The card integers are passed to the cards object to return the actual card contextual information. Each card is added to a dictionary containing the 9 cards in the players hand for each round
-select_player_deal: Slices the dealt cards for the next 9 cards, as determined by the player number

Player methods

- choose_cards: Determines the number of cards in their hand (contingent on which round it is (9/7/5/3)) and randomly chooses two. To be replaced by AI logic. Outputs both the positional reference in the hand for the two cards (e.g., 1-9) and the actual card information of the two cards
- play_card: Iterates of the two cards, using the actual card information. The card data is extracted and then iterates over the three slots on the card and updates the correspoinding board attribute slots with the attribute data.
- remove_cards: Builds a new hand dictionary by iterating over the existing hand. Uses the positional reference of the selected cards to skip the two cards that were chosen. This is essential because if a player has two of the same card type in their hand, only the one 'played' is removed. The new dictionary is then set as the players hand (effectively removing the two played cards)
- calculate_attribute_totals: Creates a blank copy of the attribute total values in the board object. Then iterates over each attribute_slot and adding that value to the attribute totals to get the total value of the attribute across the entire player board. Then sets the actual attribute totals values in the player board object to the newly calculated values


2) game.py

Defines the Game, where all the control flow occurs. A Game consists of all the high level objects, currently:
- Players (a dictionary of player objects)
- Total players (an int for the player count)

Game contains the following methods:
- play_game: Iterates over all the rounds and calls the play_round method
- play_round: iterates over all the turns and calls the play_turn method
- play_turn: Calls the 3 methods that make up a turn: card_phase, pass_hand and event_plhase
- card_phase: iterates over each player and calls the player methods of: choose_cards, play_cards, remove_cards and calculate_attribute_totals
pass_hand: Moves each hand one player 'down' (with player 1 getting the last players cards)
event_phase: TBD