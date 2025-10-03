import program_functions

MAX_CHARS = 85
MAX_WORD_LEN = 5

def assistant_display(guesses_made, guesses, confirmed_letters, word_list):
    """
    :param a: The guesses remaining
    :type a: int
    :param b: The guesses made by the user
    :type b: Array of strings
    :param c: The green letters confirmed to be in the word
    :type c: Array of 1 character strings of length 5
    :param d: The master word list
    :type d: Array of 5 letter strings
     
    A function that displays important statistics and data in regards to the assistant
    """
    print(word_list)
    print("-" * MAX_CHARS)
    print(" Number of Guesses: " + str(guesses_made+1) + "/6")
    print("-" * MAX_CHARS)
    if guesses_made == 0:
        print(" Words Guessed: ")
    else: 
        print(" Words Guessed: " + program_functions.convert_to_string(guesses)) 
    print("-" * MAX_CHARS)
    print(" Confirmed Letters: " + "".join(confirmed_letters))
    print("-" * MAX_CHARS)
                