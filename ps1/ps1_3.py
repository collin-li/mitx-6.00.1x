# PROBLEM
#
# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters 
# occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
# program should print:
#
# 'Longest substring in alphabetical order is: beggh'
#
# In case of ties, print the first substring. For example, if s = 'abcbcd', 
# then your program should print:
#
# 'Longest substring in alphabetical order is: abc'
    
# For test purposes
s = 'azcbobobegghakl'

# SOLUTION

if len(s) > 1:
    
    substring = s[0]
    length = 1

    # Store initial solution
    bestsubstring = substring
    bestlength = length
    
    for num in range(len(s)-1): # Last letter is checked by 2nd-last letter
        if s[num] <= s[num+1]:
            substring = substring + s[num+1]
            length += 1
            if length > bestlength:
                bestsubstring = substring
                bestlength = length
        else: # Reset substring and length
            substring = s[num+1]
            length = 1
            
else:
    bestsubstring = s

print ('Longest substring in alphabetical order is: ' + bestsubstring)
