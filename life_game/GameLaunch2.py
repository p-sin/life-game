###########################################################################################################
#################################################  TITLE  #################################################
###########################################################################################################

# The life game
# Created by: Philip Sinfield

###########################################################################################################
################################################  INTRO  ##################################################
###########################################################################################################

# THIS IS THE MASTER CONTROL FOR THE GAME.
# YOU CAN RUN THE GAME IN AI MODE, WHICH WILL INITIATE THE CONFIGURATION OF THE AI LOGIC
# YOU CAN RUN THE GAME IN TEST MOST, WHICH WILL TEST THE CODE AND LOGIC
# YOU CAN HAVE THE COMPUTER PLAY AGAINST ITSELF UTILISING VARIOUS AI CONFIGURATIONS
# AS PART OF THE GAME SET UP, YOU WILL CHOOSE HOW MANY PLAYERS AND ITERATIONS TO RUN

# THE CODE WILL WRITE OUT CSV FILES TO CONTAINING THE OUTPUTS TO THE SAME FOLDER CONTAINING THE CODE

###########################################################################################################
#################################################  SETUP  #################################################
###########################################################################################################

# Import required python packages
import pandas as pd
from pathlib import Path
import datetime
from datetime import datetime
import os
from GameControl import GameControl
import Functions as F

# Set path variables
CodePath = os.getcwd()  # Path of the folder containing the code
TestingFilePath = Path(CodePath + "/Testing")
OutcomeFilePath = Path(CodePath + "/OutcomeTable")

# Set timestamp for output file names
TimeStamp = datetime.now().timestamp()

# Read blank player board and outcome table
OutcomeTable = pd.read_csv("OutcomeTable/OutcomeTable.csv")
PlayerBoard = pd.read_csv("PlayerBoard/PlayerBoard.csv")

# Allows the setting of the code to test mode, which will utilise fixed inputs to test against.
# Otherwise will prompt for further configuration data for running the game
TestingFlag = input("Would you like to run the code in test mode?")
if TestingFlag.upper() == "NO":
    Testing = "No"

    Players = int(input("How many players would you like to simulate (2-6)?"))
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

    Iterations = int(input("How many iterations would you like to run?"))

else:
    Testing = "Yes"
    Players = 6
    Iterations = 1
    print("Testing: Set players to 6 and iterations to 1.")

# Sets the current iteration to 1. You shouldn't change this, but won't break anything if you do - you'll
# just start counting from a different number.
CurrentIteration = 1

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
        ) = GameControl(Players, PlayerBoard, CurrentIteration, OutcomeTable, Testing)

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
        ) = GameControl(Players, PlayerBoard, CurrentIteration, OutcomeTable, Testing)
        CurrentIteration = CurrentIteration + 1


# Writes the outcome table to a csv file, the file path is the one defined above, with the timestamp included
# as part of the file name.
OutcomeTable.to_csv(Path(OutcomeFilePath, "OutcomeTable_" + str(TimeStamp) + ".csv"))


###########################################################################################################
###############################################  ANALYSIS  ################################################
###########################################################################################################

# Placeholder for evaluation of the outcome table


exit_command = input("CS test has completed successfully. Press ENTER to exit.")
