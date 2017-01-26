# PROBLEM
#
# First, implement the function isWordGuessed that takes in two parameters - a 
# string, secretWord, and a list of letters, lettersGuessed. This function 
# returns a boolean - True if secretWord has been guessed (ie, all the letters) 
# of secretWord are in lettersGuessed) and False otherwise.
#
# For this function, you may assume that all the letters in secretWord and 
# lettersGuessed are lowercase.

# SOLUTION
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretGuessed = True # Default result until proven otherwise
    
    num = 0
    while num < len(secretWord) and secretGuessed: # Terminate loop early if a letter is not guessed
        if not secretWord[num] in lettersGuessed:
            secretGuessed = False
        num += 1
        
    return secretGuessed
