import program_functions
from time import sleep

MAX_CHARS = 85
MAX_WORD_LEN = 5
INVALID = "Invalid"

def main_menu():
    """
    A function that displays the main menu of the program

    :return: The menu option used to navigate through this menu
    :rtype: string
    """
    while True:
        print("\n Welcome to the Wordle Assistant!")
        print("-" * MAX_CHARS)
        print(" 1) Assist Today's Wordle")
        print(" 2) Settings")
        print(" 3) Exit Program")
        print("-" * MAX_CHARS)
        print(" Created by Christian Garcia - https://github.com/chrgarcia19")
        print("-" * MAX_CHARS)

        # Get user selection
        options = ["1", "2", "3"]
        selection = input(" Select an option (1-3): ").strip()
        # Validate user input
        try:
            if selection not in options:
                raise ValueError
            else:
                return selection
        except ValueError: # Something is entered that is not "1" or "2"
            print(" Invalid selection. Please try again.")
            sleep(2)
            program_functions.clear()

def assistant_display(guesses_made, guesses, confirmed_letters, word_list):
    """
    :param a: The guesses remaining
    :type a: int
    :param b: The guesses made by the user
    :type b: Array of strings
    :param c: The green letters confirmed to be in the word
    :type c: Array of 1 character strings of length 5
    :param d: The master word list
    :type d: Array of 5 letter strings
     
    A function that displays important statistics and data in regards to the assistant
    """
    print(word_list)
    print("-" * MAX_CHARS)
    print(" Number of Guesses: " + str(guesses_made+1) + "/6")
    print("-" * MAX_CHARS)
    print(" Words Guessed: " + " | ".join(guesses))
    print("-" * MAX_CHARS)
    print(" Confirmed Letters: " + "".join(confirmed_letters))
    print("-" * MAX_CHARS)
                