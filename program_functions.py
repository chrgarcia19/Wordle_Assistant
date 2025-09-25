from os import system, name
import sys
from time import sleep

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
    print("Exiting program...")
    sys.exit()

def guess():
    """
    A function that handles the guessing and validation of guesses

    :return: The lowercase and stripped version of the user's guess
    :rtype: string
    """
    guess = input("Guess a word: ").lower().strip()
    try: 
        if (len(guess) != 5):
            raise ValueError
        elif not guess.isalpha():
            raise TypeError
        else:
            return guess
    except ValueError:
        print("A guess must be 5 letters!")
        sleep(2)
        clear()
    except TypeError:
        print("A guess must contain only letters!")
        sleep(2)
        clear()

def color():
    """
    A function that handles the input and validation of the corresponding color string related to guess

    :return: The uppercase and stripped version of the user's corresponding colors
    :rtype: string
    """
    allowed = ["B", "Y", "G"]
    color = input("Enter the color corresponding to each letter (Black = b | Yellow = y | Green = g): \n").upper().strip()
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
        print("A color matching sequence should be 5 characters!")
    except TypeError:
        print("A color matching sequence must contain only b, y, or g")
    except Exception:
        print("A color matching sequence must contain only b, y, or g")
    
        