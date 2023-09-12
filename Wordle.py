# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    #CORRECT_COLOR = "#66BB66" 
    #PRESENT_COLOR = "#CCBB66" 
    #MISSING_COLOR = "#999999"
    # Creates randWord and is assigned a random word from the dictionary and makes the word all uppercase.
    randWord = random.choice(FIVE_LETTER_WORDS).upper()
    # Turns the random word into a list to separate the word into characters.
    listRandWord = list(randWord)
    # Takes User Input and checks to see if it is a word listed in the dictionary
    def enter_action(s):
        userInput = s
        if userInput.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Good Guess!")
        else: 
            gw.show_message("Not a word!")
        #userInputList = list(userInput)
        

    gw = WordleGWindow()
    # Testing purpose
    print(listRandWord)
    # Goes through a nested loop to print the random word selected from the dictionary to the wordle grid.
    for x in range(N_COLS):
        for y in range(N_ROWS - 5):
            char = listRandWord[x]
            gw.set_square_letter(y, x, char)
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
