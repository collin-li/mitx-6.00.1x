# PROBLEM
#
# Now you will implement the function hangman, which takes on parameter - the 
# secretWord the user is to guess. This starts up an interactive game of 
# Hangman between the user and the computer. Be sure you take advantage of the 
# three helper functions, isWordGuessed, getGuessedWord, and 
# getAvailableLetters, that you've defined in the previous part.

# Import functions from earlier problems
from ps3_1 import isWordGuessed
from ps3_2 import getGuessedWord
from ps3_3 import getAvailableLetters

# For test purposes
secretWord = 'apple'

# SOLUTION
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # Game introduction
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', str(len(secretWord)), 'letters long.')
    
    # Game guess and check loop
    lettersGuessed = []
    mistakesMade = 0
    
    while not isWordGuessed(secretWord, lettersGuessed) and mistakesMade < 8: # Terminate upon win or loss
        # Outline remaining guesses and available letters
        print('-------------')
        print('You have', str(8 - mistakesMade), 'guesses left')
        print('Available letters:', getAvailableLetters(lettersGuessed))

        guess = input('Please guess a letter: ').lower() # Accept upper case and lower case inputs

        # Evaluate guess
        if guess in getAvailableLetters(lettersGuessed): # Check for legal guess
            lettersGuessed += [guess]
            if guess in secretWord: # Correct guess
                print('Good guess:', getGuessedWord(secretWord,lettersGuessed))
            else: # Incorrect guess
                print('Oops! That letter is not in my word:', getGuessedWord(secretWord,lettersGuessed))
                mistakesMade += 1
                
        elif guess in lettersGuessed: # Force user to retry if guess is repeated
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord,lettersGuessed))
            
        else: # Force user to retry if guess is not a letter
            print("Sorry, that's not a letter:", getGuessedWord(secretWord,lettersGuessed))

    # Conclusion
    print('-------------')
    if isWordGuessed(secretWord, lettersGuessed): # Win
        print('Congratulations, you won!')
    else: # Lose
        print('Sorry, you ran out of guesses. The word was', secretWord)
        
hangman(secretWord)