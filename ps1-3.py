# PROBLEM
#
# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters occur in 
# alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print:
#
# 'Longest substring in alphabetical order is: beggh'
#
# In case of ties, print the first substring. For example, if s = 'abcbcd', then your
# program should print
#
# 'Longest substring in alphabetical order is: abc'
    
# For test purposes
s = 'azcbobobegghakl'

# SOLUTION

if len(s) > 1:
    
    bestsubstring = s[0]
    bestlength = 1
    length = 1
    
    for num in range(0, len(s)-1):
        if s[num] <= s[num+1]:
            length += 1
            if length > bestlength:
                bestlength = length
                bestsubstring = s[num+2-length:num+2]
        else:
            length = 1
            
else:
    bestsubstring = s

print ('Longest substring in alphabetical order is: ' + bestsubstring)
