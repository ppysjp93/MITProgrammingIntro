# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    count = 0
    for letter in letters_guessed:
        count += secret_word.count(letter)
        
    if count == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    i = 0
    letters_guessed_dict = {} 
    for char in secret_word:
        for letter in letters_guessed:
            if char == letter:
                letters_guessed_dict[i] = letter
        i += 1 
        
    guessed_so_far = ""
    j = 0
    while j < len(secret_word):
        s = letters_guessed_dict.get(j, "_ ")
        guessed_so_far += s 
        j += 1
        
    return guessed_so_far



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    remove_letters_dict = {}
    for letter in letters_guessed:
        i = 0
        for char in string.ascii_lowercase:
            if letter == char:
                remove_letters_dict[i] = letter 
            i += 1
    
    available_letters = "" 
    i = 0 
    for letter in string.ascii_lowercase:
        if remove_letters_dict.get(i, "") == letter:
            i += 1 # still needs to increment otherwise will be out of sync
            continue 
        else:
            available_letters += letter
        i += 1
            
    return available_letters
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("""
          Welcome to the game Hangman! 
          The secret word has {0} letters in it.
          --------------------------------------
          """.format(len(secret_word)))
    
    letters_guessed = []
    num_Guesses = 6
    available_letters = get_available_letters(letters_guessed)
    num_Warnings = 3
    
    while not is_word_guessed(secret_word, letters_guessed) and num_Guesses != 0:       
        begin_round(num_Guesses,available_letters)       
        guess = str.lower(input("Please guess a letter: "))       
        num_Guesses, num_Warnings, valid_guess = is_invalid_guess(guess, \
                                            letters_guessed, secret_word,\
                                            num_Warnings,num_Guesses)        
        if not valid_guess:
            continue           
        letters_guessed.append(guess)        
        available_letters = get_available_letters(letters_guessed)         
        num_Guesses = guess_in_secret_word(guess, secret_word, num_Guesses, letters_guessed)        
        print("------------------------------------------------------------")
        
    game_won_or_lost(num_Guesses,secret_word)
    
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def is_invalid_guess(guess, letters_guessed, secret_word, num_Warnings, num_Guesses):
        if not is_guess_alpha(guess):
            
            valid_guess = False      
            num_Warnings,num_Guesses = update_warnings(num_Warnings, num_Guesses)
            print("Oops! That is not a valid letter. You have {0} warnings left: {1}"\
                  .format(num_Warnings, get_guessed_word(secret_word, letters_guessed)))
                
        elif is_guess_in_letters_guessed(guess, letters_guessed):
            
            valid_guess = False
            num_Warnings, num_Guesses = update_warnings(num_Warnings, num_Guesses)
            print("Oops! You have already guessed that letter. You have {0} warnings left: {1}"\
                  .format(num_Warnings, get_guessed_word(secret_word, letters_guessed)))
                
        else:
            valid_guess = True 
        return num_Guesses, num_Warnings, valid_guess


def begin_round(num_Guesses,available_letters):
    print("""
    You have {0} guesses left.
    Available letters: {1}
    """.format(num_Guesses,available_letters))
    

def update_warnings(num_Warnings, num_Guesses):
    num_Warnings -= 1
    if (num_Warnings == 0):
        print("You have been warned 3 times. You now lose a guess and warnings \
              reset to 3.")
        num_Guesses -= 1
        num_Warnings = 3
    return num_Warnings, num_Guesses


def is_guess_in_letters_guessed(guess, letters_guessed):
    if guess in letters_guessed:
        return True
    else:
        return False

def guess_in_secret_word(guess, secret_word, num_Guesses, letters_guessed):
    if guess not in secret_word:
        num_Guesses -= 1
        print("Oops! That letter is not in my word: {0}"\
                  .format(get_guessed_word(secret_word, letters_guessed)))
        return num_Guesses
    else:
        print("Good Guess: {0}"\
                  .format(get_guessed_word(secret_word, letters_guessed)))
        return num_Guesses
    
def game_won_or_lost(num_Guesses, secret_word):
    if num_Guesses == 0:
        print("Bad luck, you lose! The secret word was '{0}'".format(secret_word))
    else:
        print("Congratulations! You win!")

def is_guess_alpha(guess):
    if len(guess) == 1 and str.isalpha(guess):
        return True
    else:
        return False


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    
    
    # secret_word = 'apple'
    # letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    # #letters_guessed = ['a', 'p', 'l', 'e']
    # print(is_word_guessed(secret_word, letters_guessed))
    # print(get_guessed_word(secret_word, letters_guessed))
    # print(get_available_letters(letters_guessed))
    
###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
