from os import system, name
from time import sleep
from colorama import init, Fore, Back, Style

import sys
import textwrap
import displays

init(autoreset=True)

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

def display_colored_word(word, color):
    """
    A function that applies the proper color to each character
    in the user's guess. 

    :param a: The word guessed
    :type a: string
    :param b: The color code corresponding to the word
    :type b: string

    :return: The string with each color applied to the word
    :rtype: string
    """
    final_string = ""
    for i in range(displays.MAX_WORD_LEN):
        if color[i] == "B":
            final_string += Fore.BLACK + word[i]
        elif color[i] == "Y":
            final_string += Fore.YELLOW + word[i]
        elif color[i] == "G":
            final_string += Fore.GREEN + word[i]
    return final_string

def convert_to_string(words_with_colors):
    """
    A function that strips the list from the words_with_colors dict.
    From here, it calls the display_colored_word to assign the proper
    color styles to each character. This returns a string to be
    printed on the game menu.

    :param a: The dictionary of words and their corresponding color code
    :type a: dict

    :return: The string with the appropriate color modifications
    :rtype: string
    """
    final_string = ""
    words = words_with_colors["word"]
    colors = words_with_colors["color"]
    for i in range(len(words)):
        colored_word = display_colored_word(words[i], colors[i])
        final_string += str(i+1) + ") " + (Back.WHITE + Style.BRIGHT + colored_word) + (Style.RESET_ALL + " | ")
    return final_string

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