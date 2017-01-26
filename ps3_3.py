# PROBLEM
#
# Next, implement the function getAvailableLetters that takes in one parameter 
# - a list of letters, lettersGuessed. This function returns a string that is 
# comprised of lowercase English letters - all lowercase English letters that 
# are not in lettersGuessed. Note that this function should return the letters 
# in alphabetical order.
#
# For this function, you may assume that all the letters in lettersGuessed are 
# lowercase.

# SOLUTION
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = list('abcdefghijklmnopqrstuvwxyz')
    
    for num in range(len(availableLetters)):
        if availableLetters[num] in lettersGuessed:
            availableLetters[num] = '' # Replace guessed letters with blanks
            
    return ''.join(availableLetters)
