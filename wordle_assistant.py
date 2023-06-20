from enum import Enum
from os import system, name


class Colors(Enum):
    BLACK = 1
    YELLOW = 2
    GREEN = 3


def clear():
    if name == "nt":  # windows
        _ = system("cls")
    else:  # mac and linux
        _ = system("clear")


# open wordlewords.txt file
words_file = open("wordlewords.txt", "r")
words_array = []
# extract all words into an array to be modified
for word in sorted(words_file):
    words_array.append(word.replace("\n", ""))
words_file.close()

guesses_remaining = 6
guesses_array = []
color_array = []
confirmed_letters = [""] * 5


def print_display():
    print("Guesses Remaining: " + str(guesses_remaining))
    print("-" * 75)
    print("Guesses Made: " + str(guesses_array))
    print("-" * 75)
    print("Confirmed letters: " + str(confirmed_letters))
    print("-" * 75)


def compare_string(words_array: [], guess: str, colors: []):
    for i in range(len(guess)):
        if int(colors[i]) == Colors.BLACK.value:
            for word in words_array[:]:
                if word.__contains__(guess[i]):
                    words_array.remove(word)
        elif int(colors[i]) == Colors.GREEN.value:
            confirmed_letters.__setitem__(i, guess[i])
            for word in words_array[:]:
                if guess[i] != word[i]:
                    words_array.remove(word)
        elif int(colors[i]) == Colors.YELLOW.value:
            for word in words_array[:]:
                if word.__contains__(guess[i]) and guess[i] == word[i]:
                    words_array.remove(word)


if __name__ == "__main__":
    while guesses_remaining != 0:
        clear()
        if guesses_remaining <= 5:
            print(words_array)
            print("-" * 75)
        print_display()
        guess = input("Guess a word: ").lower()
        while len(guess) != 5:
            print("The word must be 5 characters!")
            guess = input("Guess a word: ").lower()
        guesses_array.append(guess)
        guesses_remaining -= 1
        color_input = input(
            "Enter the number for each color returned (1 = Black, 2 = Yellow, 3 = Green):  "
        )
        while len(guess) != 5:
            print("The word must be 5 characters!")
            color_input = input(
                "Enter the number for each color returned (1 = Black, 2 = Yellow, 3 = Green):  "
            )
        compare_string(words_array, guess, color_input)
        if color_input == "33333":
            clear()
            print_display()
            print("Congratulations! You discovered the correct word.")
            break
    else:
        clear()
        print("Game over. Try again tomorrow!")
