# PROBLEM
#
# Assume s is a string of lower case characters.
#
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', your program should print:
#
# 'Number of times bob occurs is: 2'
    
# For test purposes
s = 'azcbobobegghakl'

# SOLUTION
bobcount = 0

for num in range(len(s)-2): # Terminate 'bob' search after 3rd-last letter
    if s[num:num+3] == 'bob':
        bobcount += 1

print('Number of times bob occurs is: ' + str(bobcount))
