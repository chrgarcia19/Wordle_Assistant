import system_functions
from time import sleep

def main_menu():
    print("Welcome to the Wordle Assistant!")
    print("-" * 75)
    print("1) Assist Today's Wordle")
    print("2) Exit Program")
    print("-" * 75)
    print("Created by Christian Garcia - https://github.com/chrgarcia19")
    print("-" * 75)

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
        system_functions.clear()
        main_menu()

def assistant_display(guesses_remaining, guesses, confirmed_letters):
    print("Guesses Remaining: " + str(guesses_remaining))
    print("-" * 75)
    print("Guesses Made: " + str(guesses))
    print("-" * 75)
    print("Confirmed letters: " + str(confirmed_letters))
    print("-" * 75)
                