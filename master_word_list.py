import sys, os
from time import sleep
from menu import Menu
from program_functions import clear, wrap_word_list

def resource_path(relative_path):
    """
    Get the absolute path to wordlewords.txt
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class MasterWordList(Menu):
    def __init__(self):
        self.selection = ""
        self.letter_selection = ""
        self.word_list = []
        self.sorted_list = []
        # Import words into the game when this class is created
        self.import_words()
        self.display_list = self.word_list
    
    def import_words(self):
        # open wordlewords.txt file
        words_file = open(resource_path("wordlewords.txt"), "r")
        # extract all words into an array to be modified
        for word in sorted(words_file):
            self.word_list.append(word.replace("\n", ""))
        words_file.close()

    def show_menu(self):
        print(" 1) Starting Letter Sort | 2) Ending Letter Sort | 3) Show Original List | 4) Back")

    def show_letter_options(self):
        self.letter_selection = ""
        while True:
            # Get user selection
            value = input(" Select a letter (a-z): ").strip().lower()
            # Validate user input
            try:
                if len(value) == 1 and value.isalpha():
                    self.letter_selection = value
                    break
                else:
                    raise ValueError
            except ValueError: # A letter is not entered and is not length 1
                print(" Invalid selection. Please try again.")
                sleep(2)
                clear()

    def handle_user_selection(self):
        if self.selection == "1":
            self.show_letter_options()
            self.sort_by_starting_letter(self.letter_selection)
            self.display_list = self.sorted_list
        elif self.selection == "2":
            self.show_letter_options()
            self.sort_by_ending_letter(self.letter_selection)
            self.display_list = self.sorted_list
        elif self.selection == "3":
            self.display_list = self.word_list
        elif self.selection == "4":
            print(" Going back to game menu...")
            sleep(1)
            return

    def get_selection(self):
        options = ["1", "2", "3", "4"]
        while True:
            self.show_menu()
            # Get user selection
            value = input(" Select an option (1-4): ").strip()
            # Validate user input
            try:
                if value not in options:
                    raise ValueError
                else:
                    self.selection = value
                    break
            except ValueError: # Something is entered that is not 1-4
                print(" Invalid selection. Please try again.")
                sleep(2)
                clear()

    def sort_by_starting_letter(self, letter: str):
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

    def sort_by_ending_letter(self, letter: str):
        """
        A function that sorts the word list by the starting letter of the word.

        :param a: The user inputted letter to sort by
        :type a: string
        """
        # Clear before reassigning list
        self.sorted_list.clear()
        for word in self.word_list:
            if word.endswith(letter.lower()):
                self.sorted_list.append(word)

