from collections import Counter
from enum import Enum
from time import sleep
from colorama import Fore, Style
from program_functions import clear, exit

import displays
import program_functions

class Colors(Enum):
    BLACK = "B"
    YELLOW = "Y"
    GREEN = "G"

class GameAlgorithm:
    def __init__(self):
        self.word_list = []
        self.sorted_list = []
        self.guesses_made = 0
        self.guesses = {"word": [], "color": []}
        self.confirmed_letters = ["?"] * 5
        self.guess = "Invalid"
        self.color = "Invalid"

        # Import words into the game when this class is created
        self.import_words()

    def import_words(self):
        # open wordlewords.txt file
        words_file = open("wordlewords.txt", "r")
        # extract all words into an array to be modified
        for word in sorted(words_file):
            self.word_list.append(word.replace("\n", ""))
        words_file.close()

    def guess_word(self):
        """
        A function that handles the guessing and validation of guesses

        :return: The lowercase and stripped version of the user's guess
        :rtype: string
        """
        while True:
            self.guess = input(" Guess a word: ").lower().strip()
            try: 
                if (len(self.guess) != 5):
                    raise ValueError
                elif not self.guess.isalpha():
                    raise TypeError
                else:
                    return self.guess
            except ValueError:
                print(" A guess must be 5 letters!")
                sleep(2)
                clear()
                return "Invalid"
            except TypeError:
                print(" A guess must contain only letters!")
                sleep(2)
                clear()
                return "Invalid"

    def add_color(self):
        """
        A function that handles the input and validation of the corresponding color string related to guess

        :return: The uppercase and stripped version of the user's corresponding colors
        :rtype: string
        """
        allowed = ["B", "Y", "G"]
        while True:
            self.color = input(" Enter the color corresponding to each letter (Black = b | Yellow = y | Green = g): \n ").upper().strip()
            try:
                if (len(self.color) != 5):
                    raise ValueError
                elif not self.color.isalpha():
                    raise TypeError
                elif not all (char in allowed for char in self.color):
                    raise Exception
                else: 
                    return self.color
            except ValueError:
                print(" A color matching sequence should be 5 characters!")
                sleep(2)
                clear()
                return "Invalid"
            except TypeError:
                print(" A color matching sequence must contain only b, y, or g")
                sleep(2)
                clear()
                return "Invalid"
            except Exception:
                print(" A color matching sequence must contain only b, y, or g")
                sleep(2)
                clear()
                return "Invalid"
            
    def sort_by(self, letter: str):
        """
        A function that sorts the word list by the starting letter of the word.

        :param a: The user inputted letter to sort by
        :type a: string
        """
        # Clear before reassigning list
        self.sorted_list.clear()
        for word in self.word_list:
            if word.startswith(letter.lower()):
                self.sorted_list.append(word)

    def assistant_algorithm(self):
        while self.guesses_made < 6:
            # Set guess and color to invalid to run their respective loops
            self.guess, self.color = "Invalid", "Invalid"
            ## Data that needs printed every time a the guess()/color() is called
            while self.guess == "Invalid":
                program_functions.clear()
                wrapped_word_list = program_functions.wrap_word_list(self.word_list)
                displays.assistant_display(self.guesses_made, self.guesses, self.confirmed_letters, wrapped_word_list)
                self.guess = self.guess_word()
            while self.color == "Invalid":
                program_functions.clear()
                wrapped_word_list = program_functions.wrap_word_list(self.word_list)
                displays.assistant_display(self.guesses_made, self.guesses, self.confirmed_letters, wrapped_word_list)
                print(" Word Guessed: " + self.guess)
                self.color = self.add_color()
            self.guesses["word"].append(self.guess)
            self.guesses["color"].append(self.color)
            if self.color == "GGGGG":
                program_functions.clear()
                print(" CONGRATULATIONS!! You discovered today's Wordle!")
                print(" Today's word was: " + self.guess)
                print(" Thank you for using the Wordle Assistant! See you again soon!")
                break
            else: 
                self.compare_words()
                self.guesses_made += 1
                sleep(1)
        else:
            program_functions.clear()
            print(" GAME OVER! Try again tomorrow! Good luck!")

    def compare_words(self):
        # Count the confirmed letters before checking matches
        required_letter_counts = Counter()
        for i in range(len(self.guess)):
            if self.color[i] in (Colors.GREEN.value, Colors.YELLOW.value):
                required_letter_counts[self.guess[i]] += 1

        for i in range(len(self.guess)):
            # Check if the color is green
            if self.color[i] == Colors.GREEN.value:
                self.confirmed_letters[i] = Fore.GREEN + self.guess[i] + Style.RESET_ALL
                for word in self.word_list[:]:
                    # Check if the confirmed letter matches the same spot in each word in the word list
                    if word[i] != self.guess[i]:
                        self.word_list.remove(word)
            # Check if the color is yellow
            elif self.color[i] == Colors.YELLOW.value:
                # Modifies word list based on the letter
                for word in self.word_list[:]:
                    # Filters out words that do not contain the guess letter
                    if not word.__contains__(self.guess[i]):
                        self.word_list.remove(word)
                    # Check if the character at the guess index is the same as the one at the word index
                    if word.__contains__(self.guess[i]) and word[i] == self.guess[i]:
                        self.word_list.remove(word)
            # Check if the color is black
            elif self.color[i] == Colors.BLACK.value:
                for word in self.word_list[:]:
                    if word.count(self.guess[i]) > required_letter_counts[self.guess[i]]:
                        self.word_list.remove(word)