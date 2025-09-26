from enum import Enum
from time import sleep

import displays
import program_functions
import textwrap

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
                if word.__contains__(guess[i]):
                    words_array.remove(word)



def assistant_algorithm(guesses_remaining: int):
    while guesses_remaining > 0:
        ## Data that needs printed every iteration
        cleaned_words = " ".join(words_array)
        wrapped_word_list = textwrap.fill(cleaned_words, width=displays.MAX_CHARS)
        print(wrapped_word_list)
        print("-" * displays.MAX_CHARS)
        displays.assistant_display(guesses_remaining, words_guessed, confirmed_letters)
        guess = program_functions.guess()
        words_guessed.append(guess)
        color = program_functions.color()
        compare_words(words_array, guess, color)
        guesses_remaining -= 1
        sleep(1)
        program_functions.clear()



if __name__ == "__main__":
    selection = displays.main_menu()
    if selection == "1": # Start the Wordle Assistant
        assistant_algorithm(guesses_remaining)
        
        
        
        '''
        while guesses_remaining != 0:
            system_functions.clear()
            if guesses_remaining <= 5:
                print(words_array)
                print("-" * 75)
            displays.assistant_display(guesses_remaining, guesses_array, confirmed_letters)
            guess = input("Guess a word: ").lower()
            while len(guess) != 5:
                print("The word must be 5 characters!")
                guess = input("Guess a word: ").lower()
            guesses_array.append(guess)
            guesses_remaining -= 1
            color_input = input(
                "Enter the number for each color returned (1 = Black, 2 = Yellow, 3 = Green):  "
            )
            while len(guess) != 5:
                print("The word must be 5 characters!")
                color_input = input(
                    "Enter the number for each color returned (1 = Black, 2 = Yellow, 3 = Green):  "
                )
            compare_string(words_array, guess, color_input)
            if color_input == "33333":
                system_functions.clear()
                displays.assistant_display(guesses_remaining, guesses_array, confirmed_letters)
                print("Congratulations! You discovered the correct word.")
                break
        else:
            system_functions.clear()
            print("Game over. Try again tomorrow!")
        '''
    elif selection == "3":
        program_functions.exit() # Exit the program