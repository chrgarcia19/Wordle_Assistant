from os import system, name
import sys

def clear():
    if name == "nt":  # windows
        _ = system("cls")
    else:  # mac and linux
        _ = system("clear")

def exit():
    print("Exiting program...")
    sys.exit()