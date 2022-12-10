#!/usr/bin/env python
# coding: utf-8

###########################################################################################################
#################################################  TITLE  #################################################
###########################################################################################################

# The life game
# Created by: Philip Sinfield

###########################################################################################################
################################################  INTRO  ##################################################
###########################################################################################################

# THIS CELL IS THE MASTER CONTROL FOR THE GAME. BY RUNNING THIS CELL, ALL COMPONENTS OF THE GAME WILL RUN.
# YOU CAN CONFIGURE WHETHER TO RUN THE CODE IN TEST MODE OR NOT
# THEN HOW MANY PLAYERS AND GAME ITERATIONS YOU WISH TO RUN
# YOU ALSO NEED TO CONFIGURE THE PATH DIRECTORIES FOR YOUR COMPUTER (CHECK ALL NOTEBOOKS FOR FILEPATHS)
# THE CODE WILL WRITE OUT CSV FILES TO THESE LOCATIONS.
# THERE IS NO NEED TO ALTER ANY OF THE REMAINING CODE.


###########################################################################################################
#################################################  SETUP  #################################################
###########################################################################################################

# We import various packages that contain useful functions that can be called throughout the code.
import pandas as pd
from pathlib import Path
import datetime
import GameControl
import Functions

# If you wish to test the code, set the below variable to 'Yes', otherwise set it to 'No'.
# Setting it to 'Yes' will utilise a fixed input to ensure the code is performing as expected.
Testing = "No"
TestingFilePath = Path(
    "C:/Users/p-sin/Documents/Board Games/Life game/Executable/Testing"
)

# Reads the blank OutcomeTable, so that it can be passed into and updated by all the iterations of the game
# We want to save many OutcomeTables (one for each set of iterations), thus we need to differentiate each
# saved csv file. For this we define a fixed file path and then use a timestamp which we will append to each
# file name - these are both defined here.
OutcomeTable = pd.read_csv(
    "C:/Users/p-sin/Documents/Board Games/Life game/Executable/OutcomeTable/OutcomeTable.csv"
)
OutcomeFilePath = Path(
    "C:/Users/p-sin/Documents/Board Games/Life game/Executable/OutcomeTable"
)
TimeStamp = datetime.datetime.now().timestamp()

# Read in the generic player board to be passed into the game.
PlayerBoard = pd.read_csv("PlayerBoard//PlayerBoard.csv")

# Sets the current iteration to 1. You shouldn't change this, but won't break anything if you do - you'll
# just start counting from a different number.
CurrentIteration = 1


###########################################################################################################
################################################  CONFIG  #################################################
###########################################################################################################

# Define the number of players in the game and the number of iterations you want to run.
Players = 6
Iterations = 100

# If the game is in test mode, then defaults the values to 6 players and 1 iteration.
# Otherwise, checks that the number of players is within the allowed range (2-6). If the number is outside the
# allowed range then it is changed to either the min (2) or max (6)
if Testing == "Yes":
    Players = 6
    Iterations = 1
    print("Testing: Set players to 6 and iterations to 1.")
else:
    if Players < 2:
        Players = 2
        print(
            "Number of players is below the minimum, the number of players has been set to 2"
        )

    if Players > 6:
        Players = 6
        print(
            "Number of players is above the maximum, the number of players has been set to 6"
        )


###########################################################################################################
###############################################  EXEC GAME  ###############################################
###########################################################################################################

# Runs the game code for the number of specified iterations.
# We pass in the number of players, the current iteration (which increases by 1 on each iteration)
# and the blank player board and the latest version of the outcome tables (which is appended to on each iteration)
# The function returns the completed player boards and outcomes of that game.
if Testing == "Yes":
    for x in range(Iterations):
        (
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
        ) = GameControl.GameControl(
            Players, PlayerBoard, CurrentIteration, OutcomeTable, Testing
        )

        CurrentIteration = CurrentIteration + 1

        ChildPlayerBoards = [
            Player1ChildBoard,
            Player2ChildBoard,
            Player3ChildBoard,
            Player4ChildBoard,
            Player5ChildBoard,
            Player6ChildBoard,
        ]
        CombinedChildPlayerBoard = pd.concat(ChildPlayerBoards)
        AdolPlayerBoards = [
            Player1AdolBoard,
            Player2AdolBoard,
            Player3AdolBoard,
            Player4AdolBoard,
            Player5AdolBoard,
            Player6AdolBoard,
        ]
        CombinedAdolPlayerBoard = pd.concat(AdolPlayerBoards)

        CombinedChildPlayerBoard.to_csv(
            Path(TestingFilePath, "CombinedChildPlayerBoard" + ".csv")
        )
        CombinedAdolPlayerBoard.to_csv(
            Path(TestingFilePath, "CombinedAdolPlayerBoard" + ".csv")
        )
        CombinedPlayerBoard.to_csv(
            Path(TestingFilePath, "CombinedPlayerBoard" + ".csv")
        )

else:
    for x in range(Iterations):
        (
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
        ) = GameControl.GameControl(
            Players, PlayerBoard, CurrentIteration, OutcomeTable, Testing
        )
        CurrentIteration = CurrentIteration + 1


# Writes the outcome table to a csv file, the file path is the one defined above, with the timestamp included
# as part of the file name.
OutcomeTable.to_csv(Path(OutcomeFilePath, "OutcomeTable_" + str(TimeStamp) + ".csv"))


###########################################################################################################
###############################################  ANALYSIS  ################################################
###########################################################################################################

# Placeholder for evaluation of the outcome table
