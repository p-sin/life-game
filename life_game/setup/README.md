Life game setup module

1) components.py

Defines all the core objects required for the game

rounds - providing an iterable object with the associated hand object name (as a string). Allows for dynamically working at the 'round' level

turns - Simply provides a central place for the number of turns in a round to be defined

Attributes - This is an enum of AttributeInfo. Each AttributeInfo contains the name and value of an attribute definition which can be used in the definition of a card

BoardSections - This is an enum of BoardSectionInfo. Each BoardSectionInfo defines the physical board by splitting it into 24 slots across 9 BoardSections. Each section holds 1 card (consisting of 3 slots, or two, if it is a 'soul' body part), for a total of 24 slots. Each section represents a body part + life stage (mond/body/soul + child/adolescent/adult). It then maps its three card slots to an attribute slot. This provides the mapping between the eventual card (and its three slots) and the board (which 3 of the 24 slots does that card go into).

attribute_slots - Simply provides as pre-built dictionary structure to store the attribute information on the board. Contains the 24 slots and each slot contains a 'type' and 'value'. Type and value come from the AttributeInfo. And the BoardSectionInfo determines which attribute slots are filled in. A card will bring together these two bits of information and thus map attributes to attribute slots.

Board - One will be defined for each player and contains the attribute_slots for the player. When the player plays a card, the information from it is passed into these slots and stored. Also contains totals for each of the attributes for determining success at events

decks - These are predefined with integer lists. The deck is an abstraction and does not need to contain the actual card information. Thus the deck and the dealing of cards is done with integers (those integers mapping to the card ID). Some card numbers are duplicated here to allow for multiple copies of a card in the deck


2) cards.py

Defines the 'card_type', which is admittedly so complex that it just breaks mypy as it never knows what it is dealing with.

Each 'card' is then defined as a dictionary item

{
    Card_number - consecutive integer generating a unique id for each card type.  
                  Duplicates of individual cards are allowed inside the game
        {
            number - consecutive integer mirroring the unique id
            board_section - BOARD_SECTION enum for the section of the board the card 
                            is played in
            card_slot_X - Definition of the three slots on an individual card
                {
                    slot_number: integer drawn from the corresponding BOARD_SECTION 
                                 enum defining which slot of the board the card slots into (3 slots on a card, match to 3 consecutive slots on a board)
                    values: Attribute enum containing the name and value of the 
                            attribute residing in that card slot
                }
        }
}

Cards are the highest level of object which bring together the definitions of attributes and board sections. The card object maps attribute (names and values) to specific slots on the card (1, 2 or 3) and those slots are mapped to specific slots on the board (by virtues of the board_section), ranging from 1-24.

This allows for an individual card to be selected and the information drawn from it to tell the game which board slots to apply each attribute values to


3) logic.py

Currently empty. Will contain the components for managing the AI


4) deal.py

Contains a single function for dealing cards to each player. Deals all the cards for the entire game (child, adol and adult rounds) as they use separate card pools and no new cards are ever drawn.

Generates a dictionary item with the round as the key and its value as a list of integers, drawn from the deck list of integers. Generates 9 numbers per player.

As with the decks, this is still abstracted away from the card objects.