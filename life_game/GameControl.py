#!/usr/bin/env python
# coding: utf-8

# In[16]:


# This function controls the operation of a single iteration of the game. This function is called by the
# 'GameLaunch' notebook - the number of iterations you input determine how many times this function
# is called.

# This function primarily calls other functions, in this way it orchestrates the flow of the game.
# Using paramters in these functions we are able to re-use the same functions for the three life
# stage of the game.

import copy
import pandas as pd
from pathlib import Path
import datetime
import random
import sys
import Functions


def GameControl(Players, PlayerBoard, CurrentIteration, OutcomeTable, Testing):

    ###########################################################################################################
    ###########################################  PLAYERBOARD SETUP  ###########################################
    ###########################################################################################################

    # Make a copy of the generic playerboard. Using 'deepcopy' generates unique copies (objects), allowing
    # us to alter each version of the board (for each player) as per the cards played by that player.
    Player1Board = copy.deepcopy(PlayerBoard)
    Player2Board = copy.deepcopy(PlayerBoard)
    Player3Board = copy.deepcopy(PlayerBoard)
    Player4Board = copy.deepcopy(PlayerBoard)
    Player5Board = copy.deepcopy(PlayerBoard)
    Player6Board = copy.deepcopy(PlayerBoard)

    # Update the 'Player' column in each board with the respective player number.
    Player1Board["Player"] = 1
    Player2Board["Player"] = 2
    Player3Board["Player"] = 3
    Player4Board["Player"] = 4
    Player5Board["Player"] = 5
    Player6Board["Player"] = 6

    ###########################################################################################################
    #############################################  CREATE DECKS  ##############################################
    ###########################################################################################################

    # Read the attribute deck csv file to ingest all 240 attribute cards in a single dataframe.
    AttributeCardDeck = pd.read_csv("AttributeCards//AttributeCards.csv")

    # Create three separate decks, one for each life stage, by filtering on the LifeStage values.
    ChildDeck = AttributeCardDeck[AttributeCardDeck.LifeStage.eq("Child")]
    AdolDeck = AttributeCardDeck[AttributeCardDeck.LifeStage.eq("Adolescence")]
    AdultDeck = AttributeCardDeck[AttributeCardDeck.LifeStage.eq("Adult")]

    # Repeat the same process for the event cards.
    EventCardDeck = pd.read_csv("EventCards//EventCards.csv")

    ChildEventDeck = EventCardDeck[EventCardDeck.LifeStage.eq("Child")]
    AdolEventDeck = EventCardDeck[EventCardDeck.LifeStage.eq("Adolescence")]
    AdultEventDeck = EventCardDeck[EventCardDeck.LifeStage.eq("Adult")]

    ###########################################################################################################
    #############################################  SHUFFLE CARDS  #############################################
    ###########################################################################################################

    # If testing is enabled, then provides a fixed 'deal' so that the input into the test is always the same.
    # Otherwise, randomly select 9 numbers for every player. The range of numbers in each 'deal' corresponds to
    # the range of CardIDs there are in the respective AttributeCard deck (80 per life stage). Each CardID
    # identifies one unique card.Thus, the 9 * X numbers selected here will relate to the cards ultimately
    # dealt to individual players.
    if Testing == "Yes":
        ChildDeal = list(range(1, 55))
        AdolDeal = list(range(81, 135))
        AdultDeal = list(range(161, 215))
    else:
        ChildDeal = random.sample(range(1, 81), Players * 9)
        AdolDeal = random.sample(range(81, 161), Players * 9)
        AdultDeal = random.sample(range(161, 241), Players * 9)

    # Repeat for the event cards, except this is always 5 per life stage, regardless of the number of players.
    # There are 21 cards in each deck of events.
    if Testing == "Yes":
        ChildEventDeal = list(range(1, 6))
        AdolEventDeal = list(range(22, 27))
        AdultEventDeal = list(range(43, 48))
    else:
        ChildEventDeal = random.sample(range(1, 22), 5)
        AdolEventDeal = random.sample(range(22, 43), 5)
        AdultEventDeal = random.sample(range(43, 63), 5)

    ###########################################################################################################
    ###########################################  GAME ORCHESTRATION  ##########################################
    ###########################################################################################################

    # This section orchestrates all the rounds, scoring and winner calculation for the entire iteration of
    # the game.

    # Play the attribute card phase of the child life stage (selecting and playing 8 attribute cards).
    # Define the deck (dataframe of cards) and deal (list of numbers) for the child stage.
    DeckType = ChildDeck
    DealType = ChildDeal
    Stage = "Child"

    # Pass the empty player boards, deck and deal along with the number of players playing to the function.
    # The function returns the updated player boards with the 8 chosen cards played onto them.
    (
        Player1Board,
        Player2Board,
        Player3Board,
        Player4Board,
        Player5Board,
        Player6Board,
    ) = Functions.RoundControl(
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
    )

    # Play the event card phase of the child life stage (selecting and resolving 5 event cards).
    # Define the deck and deal for the child stage.
    EventDeck = ChildEventDeck
    EventDeal = ChildEventDeal

    # Pass the player boards that were output from the attribute card phase into the function, along with the
    # number of player, deck and deal. The function then returns the updated player boards ready for the next
    # life stage.
    (
        Player1Board,
        Player2Board,
        Player3Board,
        Player4Board,
        Player5Board,
        Player6Board,
    ) = Functions.EventControl(
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
    )

    if Testing == "Yes":
        Player1ChildBoard = copy.deepcopy(Player1Board)
        Player2ChildBoard = copy.deepcopy(Player2Board)
        Player3ChildBoard = copy.deepcopy(Player3Board)
        Player4ChildBoard = copy.deepcopy(Player4Board)
        Player5ChildBoard = copy.deepcopy(Player5Board)
        Player6ChildBoard = copy.deepcopy(Player6Board)

    # Repeat for the adolescent life stage
    DeckType = AdolDeck
    DealType = AdolDeal
    Stage = "Adol"

    (
        Player1Board,
        Player2Board,
        Player3Board,
        Player4Board,
        Player5Board,
        Player6Board,
    ) = Functions.RoundControl(
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
    )

    EventDeck = AdolEventDeck
    EventDeal = AdolEventDeal

    (
        Player1Board,
        Player2Board,
        Player3Board,
        Player4Board,
        Player5Board,
        Player6Board,
    ) = Functions.EventControl(
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
    )

    if Testing == "Yes":
        Player1AdolBoard = copy.deepcopy(Player1Board)
        Player2AdolBoard = copy.deepcopy(Player2Board)
        Player3AdolBoard = copy.deepcopy(Player3Board)
        Player4AdolBoard = copy.deepcopy(Player4Board)
        Player5AdolBoard = copy.deepcopy(Player5Board)
        Player6AdolBoard = copy.deepcopy(Player6Board)

    # Repeat for the adult life stage
    DeckType = AdultDeck
    DealType = AdultDeal
    Stage = "Adult"

    (
        Player1Board,
        Player2Board,
        Player3Board,
        Player4Board,
        Player5Board,
        Player6Board,
    ) = Functions.RoundControl(
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
    )

    EventDeck = AdultEventDeck
    EventDeal = AdultEventDeal

    (
        Player1Board,
        Player2Board,
        Player3Board,
        Player4Board,
        Player5Board,
        Player6Board,
    ) = Functions.EventControl(
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
    )

    # Calculate the winner of the game and append the games metrics to the outcome table
    (
        OutcomeTable,
        Outcome,
        VictoriousPlayer,
        CombinedPlayerBoard,
    ) = Functions.CalculateWinner(
        CurrentIteration,
        OutcomeTable,
        Player1Board,
        Player2Board,
        Player3Board,
        Player4Board,
        Player5Board,
        Player6Board,
    )

    # Return the updated outcome table to the 'GameLaunch' notebook
    if Testing == "Yes":
        return (
            OutcomeTable,
            Outcome,
            VictoriousPlayer,
            CombinedPlayerBoard,
            Player1Board,
            Player2Board,
            Player3Board,
            Player4Board,
            Player5Board,
            Player6Board,
            Player1ChildBoard,
            Player2ChildBoard,
            Player3ChildBoard,
            Player4ChildBoard,
            Player5ChildBoard,
            Player6ChildBoard,
            Player1AdolBoard,
            Player2AdolBoard,
            Player3AdolBoard,
            Player4AdolBoard,
            Player5AdolBoard,
            Player6AdolBoard,
        )
    else:
        return (
            OutcomeTable,
            Outcome,
            VictoriousPlayer,
            CombinedPlayerBoard,
            Player1Board,
            Player2Board,
            Player3Board,
            Player4Board,
            Player5Board,
            Player6Board,
        )
