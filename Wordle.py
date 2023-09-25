# File: Wordle.py
from tkinter import *
from tkinter import messagebox


"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

# Creating a dictionary to hold how many guesses each play took
# The key is the number of guesses and the value is how many games they have played in one sitting for each of those number of guesses
guess_num = 0
stats_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

def wordle():
    # Creates randWord and is assigned a random word from the dictionary and makes the word all uppercase.
    randWord = random.choice(FIVE_LETTER_WORDS).upper()
    # Turns the random word into a list to separate the word into characters.
    listRandWord = list(randWord)
    # Takes User Input and checks to see if it is a word listed in the dictionary
    def enter_action(s):
        # Creating a variable to track how many guesses each game takes for them to win
        global guess_num
        guess_num = guess_num + 1
        # trueOrFalse = bool
        # if gw.switch(trueOrFalse) == True:
        #     print("True")
        correctColor = "#66BB66" 
        presentColor = "#CCBB66" 
        missingColor = "#999999"
        # else:
        #     print("False")
        #     correctColor = "#CCBB66" 
        #     presentColor = "#66BB66"
        userInput = s
        current_row = gw.get_current_row()
        # Looping through to color each of the squares for each guess
        if userInput.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Good Guess!")
            for col, letter in enumerate(userInput):
                for col1, letter1 in enumerate(randWord):
                    if letter == letter1:
                        if col == col1:
                            gw.set_square_color(current_row, col, correctColor)
                        else:
                            if gw.get_square_color(current_row, col) != correctColor:
                                gw.set_square_color(current_row, col, presentColor)

            # Message box asking to replay                                         
            if userInput == randWord:
                gw.show_message("Congrats! You guessed the word!") 
                play_again = messagebox.askyesno(title="Replay", message="Play Again?")
                # Looping through and updating the value in the dictionary and restarting the game
                if play_again: 
                    wordle()
                    stats_dict.update({guess_num:stats_dict.get(guess_num) + 1})
                    guess_num = 0
                    stats_message = ""
                    for key, value in stats_dict.items():
                        stats_message += str(key) + " guesses " + str(value) + " times\n"

                    # Messagebox showing the stats after each round
                    messagebox.showinfo(title="Your Stats", message=stats_message)
                else:
                    quit

            gw.set_current_row(current_row + 1)
    
        else: 
            gw.show_message("Not a word!")
        #userInputList = list(userInput)
        

    gw = WordleGWindow()
    # Testing purpose
    print(listRandWord)
    # Goes through a nested loop to print the random word selected from the dictionary to the wordle grid.
    # for x in range(N_COLS):
    #     for y in range(N_ROWS - 5):
    #         char = listRandWord[x]
    #         gw.set_square_letter(y, x, char)
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
