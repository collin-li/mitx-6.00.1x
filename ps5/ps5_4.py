# PROBLEM
#
# Now that you have all the pieces to the puzzle, please use them to decode the 
# file story.txt. The helper code contains a function get_story_string() that 
# returns the encrypted version of the story as a string. Create a 
# CiphertextMessage object using the story string and use decrypt_message to 
# return the appropriate shift value and unencrypted story string.

# Import function from helper code and classes from earlier problem
from ps5_0 import get_story_string
from ps5_2 import PlaintextMessage
from ps5_3 import CiphertextMessage

# SOLUTION
def decrypt_story():
    encryptedStory = CiphertextMessage(get_story_string())
    return encryptedStory.decrypt_message()

# END SOLUTION
    
# Test cases developed by the MITx 6.00.1x course

# Testing PlaintextMessage
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
# Testing CiphertextMessage
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())

# Testing decrypt_story
print(decrypt_story())
