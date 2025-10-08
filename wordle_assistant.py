from main_menu import MainMenu

from program_functions import clear
from screen_size import ScreenSize

if __name__ == "__main__":
    window = ScreenSize()
    window.set_screen_size()
    while True:
        clear()
        main = MainMenu()
        main.get_selection()
        main.handle_user_selection()