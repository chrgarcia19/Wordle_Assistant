from abc import ABC, abstractmethod

class Menu(ABC):
    def __init__(self):
        self.selection = ""
        self.MAX_CHARS = 85

    @abstractmethod
    def show_menu(self):
        """
        A function that displays the specific menu that is needed.
        """
        pass

    @abstractmethod
    def get_selection(self):
        """
        A function that gets the users input and runs it through validation
        before assigning it to selection.
        """
        pass

    @abstractmethod
    def handle_user_selection(self):
        """
        A function that handles the user input to perform the correct menu options
        """
        pass