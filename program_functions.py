from os import system, name
from time import sleep

import sys
import textwrap
import displays

def wrap_word_list(word_list):
    """
    A function that takes an array of words and combines them
    into a string for a neat display
    :param a: An array of 5 letter strings
    :type a: string array

    :return: The joined string from the array
    :rtype: string
    """
    cleaned_words = " ".join(word_list)
    return textwrap.fill(cleaned_words, width=displays.MAX_CHARS, initial_indent=" ", subsequent_indent=" ")

def clear():
    """
    Clear the terminal based on the users operating system.
    """
    if name == "nt":  # windows
        _ = system("cls")
    else:  # mac and linux
        _ = system("clear")

def exit():
    """
    Exits the program.
    """
    print(" Exiting program...")
    sys.exit()

def guess():
    """
    A function that handles the guessing and validation of guesses

    :return: The lowercase and stripped version of the user's guess
    :rtype: string
    """
    while True:
        guess = input(" Guess a word: ").lower().strip()
        try: 
            if (len(guess) != 5):
                raise ValueError
            elif not guess.isalpha():
                raise TypeError
            else:
                return guess
        except ValueError:
            print(" A guess must be 5 letters!")
            sleep(2)
            clear()
            return displays.INVALID
        except TypeError:
            print(" A guess must contain only letters!")
            sleep(2)
            clear()
            return displays.INVALID

def color():
    """
    A function that handles the input and validation of the corresponding color string related to guess

    :return: The uppercase and stripped version of the user's corresponding colors
    :rtype: string
    """
    allowed = ["B", "Y", "G"]
    while True:
        color = input(" Enter the color corresponding to each letter (Black = b | Yellow = y | Green = g): \n ").upper().strip()
        try:
            if (len(color) != 5):
                raise ValueError
            elif not color.isalpha():
                raise TypeError
            elif not all (char in allowed for char in color):
                raise Exception
            else: 
                return color
        except ValueError:
            print(" A color matching sequence should be 5 characters!")
            sleep(2)
            clear()
            return displays.INVALID
        except TypeError:
            print(" A color matching sequence must contain only b, y, or g")
            sleep(2)
            clear()
            return displays.INVALID
        except Exception:
            print(" A color matching sequence must contain only b, y, or g")
            sleep(2)
            clear()
            return displays.INVALID
    
        