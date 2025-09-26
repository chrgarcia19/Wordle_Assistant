import program_functions
from time import sleep

MAX_CHARS = 71

def main_menu():
    """
    A function that displays the main menu of the program

    :return: The menu option used to navigate through this menu
    :rtype: string
    """
    print("Welcome to the Wordle Assistant!")
    print("-" * MAX_CHARS)
    print("1) Assist Today's Wordle")
    print("2) Exit Program")
    print("-" * MAX_CHARS)
    print("Created by Christian Garcia - https://github.com/chrgarcia19")
    print("-" * MAX_CHARS)

    # Get user selection
    options = ["1", "2"]
    selection = input("Select an option (1-2): ").strip()
    # Validate user input
    try:
        if selection not in options:
            raise ValueError
        else:
            return selection
    except ValueError: # Something is entered that is not "1" or "2"
        print("Invalid selection. Please try again.")
        sleep(2)
        program_functions.clear()
        main_menu()

def assistant_display(guesses_remaining, guesses, confirmed_letters):
    """
    A function that displays important statistics and data in regards to the assistant
    """
    print("Guesses Remaining: " + str(guesses_remaining))
    print("-" * MAX_CHARS)
    print("Guesses Made: " + " | ".join(guesses))
    print("-" * MAX_CHARS)
    print("Confirmed letters: " + "".join(confirmed_letters))
    print("-" * MAX_CHARS)
                