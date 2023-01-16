#!/usr/bin/env python
# coding: utf-8

# In[2]:


# This function orchestrates the overall flow of an entire round of playing attribute cards
# (e.g child, adolescent, or adult).

import pandas as pd
from pathlib import Path
import datetime
import random
import copy
import sys


def RoundControl(
    Players,
    Player1Board,
    Player2Board,
    Player3Board,
    Player4Board,
    Player5Board,
    Player6Board,
    DeckType,
    DealType,
    Testing,
):
    # First we assign cards to each player to define their hand. We previously 'shuffled' the cards to provide a
    # deck of (players * 9) cards. We can just assign 9 cards to each player.
    # Most of the functions follow the same pattern: We iterate through each player in the game, passing in their
    # cards/board (as needed) into a generic function which executes a series of actions.

    CurrentPlayer = 1

    for x in range(6):
        if CurrentPlayer == 1:
            StartCard = 0
            EndCard = 9
            Player1Hand, Player1CardNums = DealPlayerHands(
                DealType, DeckType, StartCard, EndCard
            )

        if CurrentPlayer == 2:
            StartCard = 9
            EndCard = 18
            Player2Hand, Player2CardNums = DealPlayerHands(
                DealType, DeckType, StartCard, EndCard
            )

        if CurrentPlayer == 3:
            StartCard = 18
            EndCard = 27
            Player3Hand, Player3CardNums = DealPlayerHands(
                DealType, DeckType, StartCard, EndCard
            )

        if CurrentPlayer == 4:
            StartCard = 27
            EndCard = 36
            Player4Hand, Player4CardNums = DealPlayerHands(
                DealType, DeckType, StartCard, EndCard
            )

        if CurrentPlayer == 5:
            StartCard = 36
            EndCard = 45
            Player5Hand, Player5CardNums = DealPlayerHands(
                DealType, DeckType, StartCard, EndCard
            )

        if CurrentPlayer == 6:
            StartCard = 45
            EndCard = 54
            Player6Hand, Player6CardNums = DealPlayerHands(
                DealType, DeckType, StartCard, EndCard
            )

        CurrentPlayer = CurrentPlayer + 1

    # Next the player needs to select two cards to play from their hand. We pass in their current hand to a
    # generic function and the logic selects a first and second card to play. We then iterate around each
    # player. This is all part of a larger loop which iterates 4 times - this encapsulates the full round of
    # playing cards (2 cards, 4 times = 8 cards played).

    for x in range(4):
        CurrentPlayer = 1

        for x in range(Players):
            if CurrentPlayer == 1:
                CurrPlayerNums = Player1CardNums
                CurrPlayerHand = Player1Hand
                (
                    Player1Card1,
                    Player1Card2,
                    Player1CardNums,
                    Player1Hand,
                ) = SelectPlayerCards(CurrPlayerNums, CurrPlayerHand, Testing)

            if CurrentPlayer == 2:
                CurrPlayerNums = Player2CardNums
                CurrPlayerHand = Player2Hand
                (
                    Player2Card1,
                    Player2Card2,
                    Player2CardNums,
                    Player2Hand,
                ) = SelectPlayerCards(CurrPlayerNums, CurrPlayerHand, Testing)

            if CurrentPlayer == 3:
                CurrPlayerNums = Player3CardNums
                CurrPlayerHand = Player3Hand
                (
                    Player3Card1,
                    Player3Card2,
                    Player3CardNums,
                    Player3Hand,
                ) = SelectPlayerCards(CurrPlayerNums, CurrPlayerHand, Testing)

            if CurrentPlayer == 4:
                CurrPlayerNums = Player4CardNums
                CurrPlayerHand = Player4Hand
                (
                    Player4Card1,
                    Player4Card2,
                    Player4CardNums,
                    Player4Hand,
                ) = SelectPlayerCards(CurrPlayerNums, CurrPlayerHand, Testing)

            if CurrentPlayer == 5:
                CurrPlayerNums = Player5CardNums
                CurrPlayerHand = Player5Hand
                (
                    Player5Card1,
                    Player5Card2,
                    Player5CardNums,
                    Player5Hand,
                ) = SelectPlayerCards(CurrPlayerNums, CurrPlayerHand, Testing)

            if CurrentPlayer == 6:
                CurrPlayerNums = Player6CardNums
                CurrPlayerHand = Player6Hand
                (
                    Player6Card1,
                    Player6Card2,
                    Player6CardNums,
                    Player6Hand,
                ) = SelectPlayerCards(CurrPlayerNums, CurrPlayerHand, Testing)

            CurrentPlayer = CurrentPlayer + 1

        # After selecting the two cards to play, we then need to action this by 'playing' them onto the
        # player's boards. We do this by passing in the two selected cards and the player's board into a
        # generic function - and iterating through each player.
        # This is still wrapped within the larger loop which iterates 4 times.

        CurrentPlayer = 1

        for x in range(Players):
            if CurrentPlayer == 1:
                PlayerBoard = Player1Board
                PlayerCard = Player1Card1
                PlayCards(PlayerBoard, PlayerCard)

                PlayerCard = Player1Card2
                PlayCards(PlayerBoard, PlayerCard)

                Player1Board = PlayerBoard

            if CurrentPlayer == 2:
                PlayerBoard = Player2Board
                PlayerCard = Player2Card1
                PlayCards(PlayerBoard, PlayerCard)

                PlayerCard = Player2Card2
                PlayCards(PlayerBoard, PlayerCard)

                Player2Board = PlayerBoard

            if CurrentPlayer == 3:
                PlayerBoard = Player3Board
                PlayerCard = Player3Card1
                PlayCards(PlayerBoard, PlayerCard)

                PlayerCard = Player3Card2
                PlayCards(PlayerBoard, PlayerCard)

                Player3Board = PlayerBoard

            if CurrentPlayer == 4:
                PlayerBoard = Player4Board
                PlayerCard = Player4Card1
                PlayCards(PlayerBoard, PlayerCard)

                PlayerCard = Player4Card2
                PlayCards(PlayerBoard, PlayerCard)

                Player4Board = PlayerBoard

            if CurrentPlayer == 5:
                PlayerBoard = Player5Board
                PlayerCard = Player5Card1
                PlayCards(PlayerBoard, PlayerCard)

                PlayerCard = Player5Card2
                PlayCards(PlayerBoard, PlayerCard)

                Player5Board = PlayerBoard

            if CurrentPlayer == 6:
                PlayerBoard = Player6Board
                PlayerCard = Player6Card1
                PlayCards(PlayerBoard, PlayerCard)

                PlayerCard = Player6Card2
                PlayCards(PlayerBoard, PlayerCard)

                Player6Board = PlayerBoard

            CurrentPlayer = CurrentPlayer + 1

        # Switches the player hands around. Concludes the larger loop.
        (
            Player1Hand,
            Player2Hand,
            Player3Hand,
            Player4Hand,
            Player5Hand,
            Player6Hand,
            Player1CardNums,
            Player2CardNums,
            Player3CardNums,
            Player4CardNums,
            Player5CardNums,
            Player6CardNums,
        ) = SwitchPlayerHands(
            Players,
            Player1Hand,
            Player2Hand,
            Player3Hand,
            Player4Hand,
            Player5Hand,
            Player6Hand,
            Player1CardNums,
            Player2CardNums,
            Player3CardNums,
            Player4CardNums,
            Player5CardNums,
            Player6CardNums,
        )

    # Returns the player boards after all 4 rounds have been played (the loop has iterated 4 times)
    return (
        Player1Board,
        Player2Board,
        Player3Board,
        Player4Board,
        Player5Board,
        Player6Board,
    )


# In[ ]:


# Takes the 5 selected event cards and resolves one at a time by taking each player and comparing their
# player board to the requirements of that event card. Assigns points to the player based on the best outcome
# they can achieve for each event.


def EventControl(
    Players,
    Stage,
    Player1Board,
    Player2Board,
    Player3Board,
    Player4Board,
    Player5Board,
    Player6Board,
    EventDeck,
    EventDeal,
    Testing,
):
    CurrentEvent = 1

    for x in range(5):
        EventDeal, EventCard = SelectEvent(EventDeck, EventDeal, Testing)

        CurrentPlayer = 1

        for x in range(Players):
            if CurrentPlayer == 1:
                PlayerBoard = Player1Board
                Player1Board = ResolveEvent(EventCard, PlayerBoard, CurrentEvent, Stage)

            if CurrentPlayer == 2:
                PlayerBoard = Player2Board
                Player2Board = ResolveEvent(EventCard, PlayerBoard, CurrentEvent, Stage)

            if CurrentPlayer == 3:
                PlayerBoard = Player3Board
                Player3Board = ResolveEvent(EventCard, PlayerBoard, CurrentEvent, Stage)

            if CurrentPlayer == 4:
                PlayerBoard = Player4Board
                Player4Board = ResolveEvent(EventCard, PlayerBoard, CurrentEvent, Stage)

            if CurrentPlayer == 5:
                PlayerBoard = Player5Board
                Player5Board = ResolveEvent(EventCard, PlayerBoard, CurrentEvent, Stage)

            if CurrentPlayer == 6:
                PlayerBoard = Player6Board
                Player6Board = ResolveEvent(EventCard, PlayerBoard, CurrentEvent, Stage)

            CurrentPlayer = CurrentPlayer + 1

        CurrentEvent = CurrentEvent + 1

    return (
        Player1Board,
        Player2Board,
        Player3Board,
        Player4Board,
        Player5Board,
        Player6Board,
    )


# In[ ]:


# Creates a list of card IDs from the 'deal' that was randomly generated. The list is defined by the start
# and end card values passed in (defined for each player to give them 9 unique cards each). Then generates a
# dataframe by filtering the 'deck' for those 9 card IDs.
def DealPlayerHands(DealType, DeckType, StartCard, EndCard):
    PlayerCardNums = DealType[StartCard:EndCard]
    PlayerHand = DeckType.loc[DeckType["CardID"].isin(PlayerCardNums)]

    return PlayerHand, PlayerCardNums


# In[3]:


# Applies the logic to select two cards from the player hand to play. If in testing mode, selects the first
# card in the list. Otherwise, currently selects randomly.


def SelectPlayerCards(CurrPlayerNums, CurrPlayerHand, Testing):
    if Testing == "Yes":
        PlayerCard1Num = [CurrPlayerNums[0]]
        CurrPlayerNums.remove(PlayerCard1Num[0])
        PlayerCard1 = CurrPlayerHand.loc[CurrPlayerHand["CardID"].isin(PlayerCard1Num)]
        CurrPlayerHand = CurrPlayerHand[CurrPlayerHand.CardID != PlayerCard1Num[0]]

        PlayerCard2Num = [CurrPlayerNums[0]]
        CurrPlayerNums.remove(PlayerCard2Num[0])
        PlayerCard2 = CurrPlayerHand.loc[CurrPlayerHand["CardID"].isin(PlayerCard2Num)]
        CurrPlayerHand = CurrPlayerHand[CurrPlayerHand.CardID != PlayerCard2Num[0]]

    else:
        PlayerCard1Num = [random.choice(CurrPlayerNums)]
        CurrPlayerNums.remove(PlayerCard1Num[0])
        PlayerCard1 = CurrPlayerHand.loc[CurrPlayerHand["CardID"].isin(PlayerCard1Num)]
        CurrPlayerHand = CurrPlayerHand[CurrPlayerHand.CardID != PlayerCard1Num[0]]

        PlayerCard2Num = [random.choice(CurrPlayerNums)]
        CurrPlayerNums.remove(PlayerCard2Num[0])
        PlayerCard2 = CurrPlayerHand.loc[CurrPlayerHand["CardID"].isin(PlayerCard2Num)]
        CurrPlayerHand = CurrPlayerHand[CurrPlayerHand.CardID != PlayerCard2Num[0]]

    return PlayerCard1, PlayerCard2, CurrPlayerNums, CurrPlayerHand


# In[ ]:


# Takes a single card and applies its effects to the player board. Either updates one attribute, or two,
# depending on the type of card. To do this, it first identifies which slot (and therefore column in the
# playerboard dataframe) is being updated - if this already contains values (which will be overwritten), it
# substracts those values from the player's attribute totals. Then it writes in the new values from the played
# card.


def PlayCards(PlayerBoard, PlayerCard):
    if PlayerCard.iloc[0]["CardType"] == 1:
        CardSlot1 = PlayerCard.iloc[0]["Attr1Slot"]
        CardAttr1 = PlayerCard.iloc[0]["Attr1"]
        CardValue1 = PlayerCard.iloc[0]["Attr1Value"]
        AttrColName1 = "Slot" + str(CardSlot1) + "Attr"
        ValueColName1 = "Slot" + str(CardSlot1) + "Value"

        OrigAttr1 = PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(AttrColName1)]
        OrigValue1 = PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(ValueColName1)]

        if OrigAttr1 != "None":
            PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(OrigAttr1)] = (
                PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(OrigAttr1)] - OrigValue1
            )

        PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(AttrColName1)] = CardAttr1
        PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(ValueColName1)] = CardValue1
        PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(CardAttr1)] = (
            PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(CardAttr1)] + CardValue1
        )

        PlayerBoard["MaxValue"] = PlayerBoard[
            [
                "Sociability",
                "Intelligence",
                "Creativity",
                "Strength",
                "Constitution",
                "Coordination",
                "Empathy",
                "Determination",
            ]
        ].max(axis=1)

    else:
        CardSlot1 = PlayerCard.iloc[0]["Attr1Slot"]
        CardAttr1 = PlayerCard.iloc[0]["Attr1"]
        CardValue1 = PlayerCard.iloc[0]["Attr1Value"]
        AttrColName1 = "Slot" + str(CardSlot1) + "Attr"
        ValueColName1 = "Slot" + str(CardSlot1) + "Value"
        CardSlot2 = PlayerCard.iloc[0]["Attr2Slot"]
        CardAttr2 = PlayerCard.iloc[0]["Attr2"]
        CardValue2 = PlayerCard.iloc[0]["Attr2Value"]
        AttrColName2 = "Slot" + str(CardSlot2) + "Attr"
        ValueColName2 = "Slot" + str(CardSlot2) + "Value"

        OrigAttr1 = PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(AttrColName1)]
        OrigValue1 = PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(ValueColName1)]

        if OrigAttr1 != "None":
            PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(OrigAttr1)] = (
                PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(OrigAttr1)] - OrigValue1
            )

        OrigAttr2 = PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(AttrColName2)]
        OrigValue2 = PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(ValueColName2)]

        if OrigAttr2 != "None":
            PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(OrigAttr2)] = (
                PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(OrigAttr2)] - OrigValue2
            )

        PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(AttrColName1)] = CardAttr1
        PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(ValueColName1)] = CardValue1
        PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(CardAttr1)] = (
            PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(CardAttr1)] + CardValue1
        )

        PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(AttrColName2)] = CardAttr2
        PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(ValueColName2)] = CardValue2
        PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(CardAttr2)] = (
            PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(CardAttr2)] + CardValue2
        )

        PlayerBoard["MaxValue"] = PlayerBoard[
            [
                "Sociability",
                "Intelligence",
                "Creativity",
                "Strength",
                "Constitution",
                "Coordination",
                "Empathy",
                "Determination",
            ]
        ].max(axis=1)

    return PlayerBoard


# In[ ]:


# Based on the number of players, this switches the player hands around.


def SwitchPlayerHands(
    Players,
    Player1Hand,
    Player2Hand,
    Player3Hand,
    Player4Hand,
    Player5Hand,
    Player6Hand,
    Player1CardNums,
    Player2CardNums,
    Player3CardNums,
    Player4CardNums,
    Player5CardNums,
    Player6CardNums,
):
    if Players == 6:
        TempCardNums = Player6CardNums
        TempHand = Player6Hand

    if Players == 5:
        TempCardNums = Player5CardNums
        TempHand = Player5Hand

    if Players == 4:
        TempCardNums = Player4CardNums
        TempHand = Player4Hand

    if Players == 3:
        TempCardNums = Player3CardNums
        TempHand = Player3Hand

    if Players == 2:
        TempCardNums = Player2CardNums
        TempHand = Player2Hand

    if Players > 5:
        Player6CardNums = Player5CardNums
        Player6Hand = Player5Hand

    if Players > 4:
        Player5CardNums = Player4CardNums
        Player5Hand = Player4Hand

    if Players > 3:
        Player4CardNums = Player3CardNums
        Player4Hand = Player3Hand

    if Players > 2:
        Player3CardNums = Player2CardNums
        Player3Hand = Player2Hand

    if Players > 1:
        Player2CardNums = Player1CardNums
        Player2Hand = Player1Hand

        Player1CardNums = TempCardNums
        Player1Hand = TempHand

    return (
        Player1Hand,
        Player2Hand,
        Player3Hand,
        Player4Hand,
        Player5Hand,
        Player6Hand,
        Player1CardNums,
        Player2CardNums,
        Player3CardNums,
        Player4CardNums,
        Player5CardNums,
        Player6CardNums,
    )


# In[ ]:


# Selects an event randomly from the 5 that were originally randomly chosen.
# If testing, then selects the first event in the list.


def SelectEvent(EventDeck, EventDeal, Testing):
    if Testing == "Yes":
        EventCardNum = [EventDeal[0]]
        EventCard = EventDeck.loc[EventDeck["EventCardID"].isin(EventCardNum)]
        EventDeal.remove(EventCardNum[0])
    else:
        EventCardNum = [random.choice(EventDeal)]
        EventCard = EventDeck.loc[EventDeck["EventCardID"].isin(EventCardNum)]
        EventDeal.remove(EventCardNum[0])

    return EventDeal, EventCard


# In[1]:


# Takes the selected event card and the player's board, checks the player's attributes to see which outcomes
# they are able to achieve. Then takes the best outcome they can achieve and adds this number of points to
# their score
def ResolveEvent(EventCard, PlayerBoard, CurrentEvent, Stage):
    EventColumn = str(Stage) + "Event" + str(CurrentEvent)

    if (
        PlayerBoard.iloc[
            0,
            PlayerBoard.columns.get_loc(
                EventCard.iloc[0, EventCard.columns.get_loc("Outcome1Attr")]
            ),
        ]
        >= EventCard.iloc[0, EventCard.columns.get_loc("Outcome1Val")]
    ):
        PlayerBoard.iloc[
            0, PlayerBoard.columns.get_loc("EventPoints")
        ] = EventCard.iloc[0, EventCard.columns.get_loc("Outcome1Points")]
        PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(EventColumn)] = 1

    if (
        PlayerBoard.iloc[
            0,
            PlayerBoard.columns.get_loc(
                EventCard.iloc[0, EventCard.columns.get_loc("Outcome2Attr")]
            ),
        ]
        >= EventCard.iloc[0, EventCard.columns.get_loc("Outcome2Val")]
    ):
        PlayerBoard.iloc[
            0, PlayerBoard.columns.get_loc("EventPoints")
        ] = EventCard.iloc[0, EventCard.columns.get_loc("Outcome2Points")]
        PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(EventColumn)] = 2

    if (
        (
            PlayerBoard.iloc[
                0,
                PlayerBoard.columns.get_loc(
                    EventCard.iloc[0, EventCard.columns.get_loc("Outcome3Attr1")]
                ),
            ]
            + PlayerBoard.iloc[
                0,
                PlayerBoard.columns.get_loc(
                    EventCard.iloc[0, EventCard.columns.get_loc("Outcome3Attr2")]
                ),
            ]
        )
        >= EventCard.iloc[0, EventCard.columns.get_loc("Outcome3Total")]
        and PlayerBoard.iloc[
            0,
            PlayerBoard.columns.get_loc(
                EventCard.iloc[0, EventCard.columns.get_loc("Outcome3Attr1")]
            ),
        ]
        >= 1
        and PlayerBoard.iloc[
            0,
            PlayerBoard.columns.get_loc(
                EventCard.iloc[0, EventCard.columns.get_loc("Outcome3Attr2")]
            ),
        ]
        >= 1
    ):
        PlayerBoard.iloc[
            0, PlayerBoard.columns.get_loc("EventPoints")
        ] = EventCard.iloc[0, EventCard.columns.get_loc("Outcome3Points")]
        PlayerBoard.iloc[0, PlayerBoard.columns.get_loc(EventColumn)] = 3

    PlayerBoard.iloc[0, PlayerBoard.columns.get_loc("TotalPoints")] = (
        PlayerBoard.iloc[0, PlayerBoard.columns.get_loc("TotalPoints")]
        + PlayerBoard.iloc[0, PlayerBoard.columns.get_loc("EventPoints")]
    )

    PlayerBoard.iloc[0, PlayerBoard.columns.get_loc("EventPoints")] = 0

    return PlayerBoard


# In[ ]:


# Combines the player boards into a single dataframe and then identifies the winning player based on the one
# with the highest score.
def CalculateWinner(
    CurrentIteration,
    OutcomeTable,
    Player1Board,
    Player2Board,
    Player3Board,
    Player4Board,
    Player5Board,
    Player6Board,
):
    CombinedPlayerBoard = [
        Player1Board,
        Player2Board,
        Player3Board,
        Player4Board,
        Player5Board,
        Player6Board,
    ]
    CombinedPlayerBoard = pd.concat(CombinedPlayerBoard)

    VictoriousPlayer = CombinedPlayerBoard.loc[
        CombinedPlayerBoard["TotalPoints"] == CombinedPlayerBoard["TotalPoints"].max()
    ]

    for x in range(len(VictoriousPlayer)):
        Row = x

        Outcome = {
            "Iteration": CurrentIteration,
            "WinningPlayer": VictoriousPlayer.iloc[
                Row, VictoriousPlayer.columns.get_loc("Player")
            ],
            "WinningScore": CombinedPlayerBoard["TotalPoints"].max(),
            "AverageScore": int(CombinedPlayerBoard["TotalPoints"].mean()),
            "LowestScore": CombinedPlayerBoard["TotalPoints"].min(),
            "HighestScore": CombinedPlayerBoard["TotalPoints"].max(),
        }

        OutcomeTable = OutcomeTable.append(Outcome, ignore_index=True)

    return OutcomeTable, Outcome, VictoriousPlayer, CombinedPlayerBoard
