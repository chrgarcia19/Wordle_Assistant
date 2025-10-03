from time import sleep
from program_functions import clear


class GameMenu:
    def __init__(self):
        self.selection = ""

    def show_game_menu(self):
        print(" 1) Sort the Word List      2) Guess a Word      3) Back to Main Menu")

    def get_selection(self):
        options = ["1", "2", "3"]
        while True:
            self.show_game_menu()
            # Get user selection
            value = input(" Select an option (1-3): ").strip()
            # Validate user input
            try:
                if value not in options:
                    raise ValueError
                else:
                    self.selection = value
                    break
            except ValueError: # Something is entered that is not "1" or "2"
                print(" Invalid selection. Please try again.")
                sleep(2)
                clear()

    def handle_user_selection(self):
        if self.selection == "1": # Sort word list menu
            pass
        elif self.selection == "2": # Guess a word
            pass
        elif self.selection == "3": # Go back to main menu
            pass
