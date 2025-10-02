from collections import Counter
from enum import Enum
from time import sleep

import displays
import program_functions

class Colors(Enum):
    BLACK = "B"
    YELLOW = "Y"
    GREEN = "G"

# open wordlewords.txt file
words_file = open("wordlewords.txt", "r")
words_array = []
# extract all words into an array to be modified
for word in sorted(words_file):
    words_array.append(word.replace("\n", ""))
words_file.close()

guesses_remaining = 6
words_guessed = []
confirmed_letters = ["?"] * 5

def compare_words(words_array, guess: str, color: str):
    # Count the confirmed letters before checking matches
    required_letter_counts = Counter()
    for i in range(len(guess)):
        if color[i] in (Colors.GREEN.value, Colors.YELLOW.value):
            required_letter_counts[guess[i]] += 1

    for i in range(len(guess)):
        # Check if the color is green
        if color[i] == Colors.GREEN.value:
            confirmed_letters[i] = guess[i]
            for word in words_array[:]:
                # Check if the confirmed letter matches the same spot in each word in the word list
                if word[i] != guess[i]:
                    words_array.remove(word)
        # Check if the color is yellow
        elif color[i] == Colors.YELLOW.value:
            # Modifies word list based on the letter
            for word in words_array[:]:
                # Filters out words that do not contain the guess letter
                if not word.__contains__(guess[i]):
                    words_array.remove(word)
                # Check if the character at the guess index is the same as the one at the word index
                if word.__contains__(guess[i]) and word[i] == guess[i]:
                    words_array.remove(word)
        # Check if the color is black
        elif color[i] == Colors.BLACK.value:
            for word in words_array[:]:
                if word.count(guess[i]) > required_letter_counts[guess[i]]:
                    words_array.remove(word)



def assistant_algorithm(guesses_remaining: int):
    while guesses_remaining > 0:
        # Set guess and color to invalid to run their respective loops
        guess, color = displays.INVALID, displays.INVALID
        ## Data that needs printed every time a the guess()/color() is called
        while guess == displays.INVALID:
            word_list = program_functions.wrap_word_list(words_array)
            displays.assistant_display(guesses_remaining, words_guessed, confirmed_letters, word_list)
            guess = program_functions.guess()
        words_guessed.append(guess)
        while color == displays.INVALID:
            word_list = program_functions.wrap_word_list(words_array)
            displays.assistant_display(guesses_remaining, words_guessed, confirmed_letters, word_list)
            print(" Word Guessed: " + guess)
            color = program_functions.color()
        if color == "GGGGG":
            program_functions.clear()
            print(" CONGRATULATIONS!! You discovered today's Wordle!")
            print(" Today's word was: " + guess)
            print(" Thank you for using the Wordle Assistant! See you again soon!")
            break
        else: 
            compare_words(words_array, guess, color)
            guesses_remaining -= 1
            sleep(1)
            program_functions.clear()
    else:
        program_functions.clear()
        print(" GAME OVER! Try again tomorrow! Good luck!")



if __name__ == "__main__":
    selection = displays.main_menu()
    if selection == "1": # Start the Wordle Assistant
        assistant_algorithm(guesses_remaining)
    elif selection == "2":
        pass
        ## Add settings 
    elif selection == "3":
        program_functions.exit() # Exit the program