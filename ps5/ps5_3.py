# PROBLEM
#
# Given an encrypted message, if you know the shift used to encode the message, 
# decoding it is trivial. If message is the encrypted message, and s is the 
# shift used to encrypt the message, then apply_shift(message, 26-s) gives you 
# the original plaintext message. Do you see why?
#
# The problem, of course, is that you don’t know the shift. But our encryption 
# method only has 26 distinct possible values for the shift! We know English is 
# the main language of these emails, so if we can write a program that tries 
# each shift and maximizes the number of English words in the decoded message, 
# we can decrypt their cipher! A simple indication of whether or not the 
# correct shift has been found is if most of the words obtained after a shift 
# are valid words. Note that this only means that most of the words obtained 
# are actual words. It is possible to have a message that can be decoded by two 
# separate shifts into different sets of words. While there are various 
# strategies for deciding between ambiguous decryptions, for this problem we 
# are only looking for a simple solution.
# 
# The methods you should fill in are:
# * __init__(self, text, shift): Use the parent class constructor to make your 
#  code more concise.
# * decrypt_message(self): You may find the helper function is_word(wordlist, 
#   word) and the string method split() useful. Note that is_word will ignore 
#   punctuation and other special characters when considering whether a word is 
#   valid.

# Import function from helper code and superclass from earlier problem
from ps5_0 import is_word
from ps5_1 import Message

# SOLUTION
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # Initialize best shift
        bestShift = 0
        mostValidWords = 0
        
        # Iterate through 26 possible shifts
        for s in range(26):
            
            # Create list of words in message
            messageWords = self.apply_shift(s).split(' ')
            
            # Count valid words in shifted message
            validWordCount = 0
            for word in messageWords:
                if is_word(self.valid_words, word):
                    validWordCount += 1
            
            # Update best shift if better decryption is found
            if validWordCount > mostValidWords:
                bestShift = s
                mostValidWords = validWordCount

                # Break loop if perfect decryption is found
                if mostValidWords == len(messageWords):
                    return (bestShift, self.apply_shift(bestShift))
            
        return (bestShift, self.apply_shift(bestShift))
