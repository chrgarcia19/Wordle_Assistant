from main_menu import MainMenu

import program_functions

if __name__ == "__main__":
    while True:
        program_functions.clear()
        main = MainMenu()
        main.get_selection()
        main.handle_user_selection()