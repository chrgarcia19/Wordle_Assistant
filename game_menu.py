from time import sleep
from menu import Menu
from program_functions import clear


class GameMenu(Menu):
    def __init__(self):
        self.selection = ""

    def show_menu(self):
        print(" 1) Sort the Word List      2) Guess a Word      3) Back to Main Menu")

    def get_selection(self):
        options = ["1", "2", "3"]
        while True:
            self.show_menu()
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