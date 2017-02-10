# PROBLEM
#
# A game consists of playing multiple hands. We need to implement one final 
# function to complete our word-game program. Write the code that implements 
# the playGame function. 
#
# Read through the specification and make sure you understand what this 
# function accomplishes. For the game, you should use the HAND_SIZE constant 
# to determine the number of cards in a hand.

# Import functions from earlier problems
from ps4_0 import *
from ps4_5 import playHand

# SOLUTION
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    gameMode = '' # Initialize user input

    # As long as the user has not chosen to end the game
    while gameMode != 'e':
        
        # Ask user to choose game mode
        gameMode = input('Enter n to deal a new hand, r to reply the last hand, or e to end game: ').lower()
        while not gameMode in list('nre'): # Enforce valid input
            print('Invalid command.')
            gameMode = input('Enter n to deal a new hand, r to reply the last hand, or e to end game: ').lower()
        
        # Initialize game if user inputted 'n' or 'r'
        if gameMode in 'nr':
            
            if gameMode == 'n': # Set new hand if user inputted 'n'
                hand = dealHand(HAND_SIZE)
            
            try: # Attempt to initialize game
                playHand(hand, wordList, HAND_SIZE)
            
            except UnboundLocalError: # If hand has not been previously set
                print('You have not played a hand yet. Please play a new hand first!')

# END SOLUTION

# Build data structures used for entire session and play game
wordList = loadWords()
playGame(wordList)
