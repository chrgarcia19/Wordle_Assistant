from time import sleep
from game_algorithm import GameAlgorithm
from menu import Menu
from program_functions import clear, exit

class MainMenu(Menu):
    def __init__(self):
        self.selection = ""
        self.MAX_CHARS = 85

    def show_menu(self):
        """
        A function that displays the main menu of the program
        """
        print("\n Welcome to the Wordle Assistant!")
        print("-" * self.MAX_CHARS)
        print(" 1) Assist Today's Wordle")
        print(" 2) Settings")
        print(" 3) Exit Program")
        print("-" * self.MAX_CHARS)
        print(" Created by Christian Garcia - https://github.com/chrgarcia19")
        print("-" * self.MAX_CHARS)

    def get_selection(self):
        """
        A function that gets the users input and runs it through validation
        before assigning it to selection
        """
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

    def handle_user_selection(self):
        """
        A function that handles the user input to perform the correct menu options
        """
        if self.selection == "1": # Start the Wordle Assistant
            game = GameAlgorithm()
            game.assistant_algorithm()
        elif self.selection == "2":
            pass
            ## Add settings 
        elif self.selection == "3":
            exit() # Exit the program
