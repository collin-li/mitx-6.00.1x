# PROBLEM
#
# At this point, we have written code to generate a random hand and display 
# that hand to the user. We can also ask the user for a word (Python's input) 
# and score the word (using your getWordScore). However, at this point we have 
# not written any code to verify that a word given by a player obeys the rules 
# of the game. A valid word is in the word list; and it is composed entirely of
# letters from the current hand. Implement the isValidWord function.

# Import functions from earlier problems
from ps4_0 import getFrequencyDict

# SOLUTION
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # Logic paths:
    # 1. Word is not in hand: return False in for loop
    # 2. Word is in hand, word is not in wordList: return False at last line
    # 3. Word is in hand, word is in wordList: return True at last line

    # Confirm word is entirely composed of letters in the hand
    wordDict = getFrequencyDict(word) # Convert word into dictionary format
    for letter in wordDict:
        if not wordDict[letter] <= hand.get(letter, 0):
            return False # Fail test and break loop and function
    
    # Check if word is in the wordList
    return word in wordList
