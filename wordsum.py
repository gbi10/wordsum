#!/usr/bin/python

##############################################################
# WORDSUM.PY written by G.B.Izatt 23/02/2019
#
# Program to find solutions to Word Sums e.g.
#
#     ROCK
#    +ROLL
#    =====
#    MUSIC
#    =====
#
# Each letter in this SUM is a DIGIT from 0-9. What solutions
# are there that make the above SUM work. That's what this 
# program is designed to find. 
# 
# root@debian/# python wordsum.py rock roll music
#  ROCK
#  ROLL
# MUSIC
# Iterating : ['R', 'O', 'C', 'K', 'L', 'M', 'U', 'S', 'I']
# ...................
# Solution Found  {'C': 2, 'I': 7, 'K': 8, 'M': 1, 'L': 4, 'O': 3, 'S': 6, 'R': 5, 'U': 0}
# Solution Found  {'C': 8, 'I': 4, 'K': 2, 'M': 1, 'L': 6, 'O': 3, 'S': 7, 'R': 5, 'U': 0}
# Solution Found  {'C': 2, 'I': 6, 'K': 9, 'M': 1, 'L': 3, 'O': 4, 'S': 8, 'R': 5, 'U': 0}....
# Solution Found  {'C': 4, 'I': 0, 'K': 9, 'M': 1, 'L': 5, 'O': 3, 'S': 7, 'R': 6, 'U': 2}
# Solution Found  {'C': 5, 'I': 3, 'K': 8, 'M': 1, 'L': 7, 'O': 4, 'S': 9, 'R': 6, 'U': 2}
# Solution Found  {'C': 2, 'I': 7, 'K': 8, 'M': 1, 'L': 4, 'O': 5, 'S': 0, 'R': 6, 'U': 3}.
# Solution Found  {'C': 0, 'I': 9, 'K': 2, 'M': 1, 'L': 8, 'O': 7, 'S': 4, 'R': 6, 'U': 3}
# Solution Found  {'C': 4, 'I': 0, 'K': 9, 'M': 1, 'L': 5, 'O': 8, 'S': 7, 'R': 6, 'U': 3}..
# Solution Found  {'C': 0, 'I': 9, 'K': 2, 'M': 1, 'L': 8, 'O': 3, 'S': 6, 'R': 7, 'U': 4}..
# Solution Found  {'C': 3, 'I': 8, 'K': 9, 'M': 1, 'L': 4, 'O': 6, 'S': 2, 'R': 7, 'U': 5}..
# Solution Found  {'C': 7, 'I': 0, 'K': 4, 'M': 1, 'L': 3, 'O': 2, 'S': 5, 'R': 8, 'U': 6}
# Solution Found  {'C': 4, 'I': 0, 'K': 9, 'M': 1, 'L': 5, 'O': 3, 'S': 7, 'R': 8, 'U': 6}
# Solution Found  {'C': 2, 'I': 0, 'K': 5, 'M': 1, 'L': 7, 'O': 4, 'S': 9, 'R': 8, 'U': 6}.
# Solution Found  {'C': 2, 'I': 6, 'K': 9, 'M': 1, 'L': 3, 'O': 5, 'S': 0, 'R': 8, 'U': 7}
# Solution Found  {'C': 4, 'I': 0, 'K': 9, 'M': 1, 'L': 5, 'O': 6, 'S': 3, 'R': 8, 'U': 7}..
# Solution Found  {'C': 3, 'I': 0, 'K': 7, 'M': 1, 'L': 6, 'O': 2, 'S': 5, 'R': 9, 'U': 8}
# Solution Found  {'C': 7, 'I': 0, 'K': 4, 'M': 1, 'L': 3, 'O': 2, 'S': 5, 'R': 9, 'U': 8}.
# Solution Found  {'C': 6, 'I': 0, 'K': 2, 'M': 1, 'L': 4, 'O': 3, 'S': 7, 'R': 9, 'U': 8}..
# Found  18  solutions
##############################################################

import sys

##############################################################
# GLOBAL VARIABLES
##############################################################
maxwordlen = 0
words = []
trimwords = []
letterlist = []
alldigits = [0,1,2,3,4,5,6,7,8,9]
countiterate = 0
solutioncount = 0
paramcount = 0
wordindex = range(1,4)

##############################################################
# SEARCH FUNCTIONS
##############################################################

# Function to check first digit is non zero
def fdnz(letter2digit,word):
    return letter2digit[word[0]] > 0
    
# Function to convert a word into a number using a dictionary of letters2digits
def word2number(letter2digit, word):
    x = 0
    for c in word:
        n = letter2digit[c]
        x = (10*x) + n
    return x

# Test to see if this combination works
def test_combination(digitlist):
    # Uses global variables
    global countiterate
    global trimwords
    global solutioncount	

    # Check letter list length same as digitlist
    # if len(letterlist) != len(digitlist):
        # print 'Fatal Error len(letterlist) != len(digitlist) => ',letterlist," : ",digitlist
        # quit()

    # Update counter
    countiterate = countiterate + 1
    if (countiterate % 100000) == 0:
        sys.stdout.write('.') 
        sys.stdout.flush()

    # Put digit list and letter list into a dictionary
    letter2digit = {}
    for i in range(0,len(digitlist)):
        letter2digit[letterlist[i]] = digitlist[i]

    # Check all the numbers first digits 
    allfdnz = True
    for i in range(0,paramcount-1):
        allfdnz = allfdnz and fdnz(letter2digit,trimwords[i])

    # Is first digit nonzero
    if allfdnz:        
        # OK now convert the trimwords to actual numbers
        wordsum = 0
        for i in range(0,paramcount-2):
            wordsum = wordsum + word2number(letter2digit,trimwords[i])

        # What about the total
        wordtotal = word2number(letter2digit,trimwords[paramcount-2])

        # If it adds up then print result
        if wordsum == wordtotal:
            solutioncount = solutioncount + 1
            print "\nSolution Found ",letter2digit,



# Recursively generate every digit combination
def recurse_digits_combinations(prelist,postlist,depth):
    # print 'Depth ',depth,' => ', prelist,' : ', postlist;
    if depth < 0:
        # Process the list
        # print prelist
        test_combination(prelist)
    else:
        # Iterate through single digit possibilities
        for i in range(0,len(postlist)):
            newprelist = prelist + [postlist[i]]
            shorterlist = list(postlist)
            del shorterlist[i]
            recurse_digits_combinations(newprelist,shorterlist,depth-1)

##############################################################
# MAIN PROGRAM
##############################################################

# Check we have the correct number of parameters
paramcount = len(sys.argv)
if paramcount < 4:
    print 'Invalid number of arguments! Must have at least 3 words.'
    quit()

# words defined
wordindex = range(1,paramcount)

# Find out length of longest
for i in wordindex:
    newwordlen = len(sys.argv[i])
    if newwordlen > maxwordlen:
        maxwordlen = newwordlen

# Create a string formatter
strformat = '%%%ds' % maxwordlen

# Convert to uppercase right justified
for i in wordindex:
    s = strformat % sys.argv[i].upper()
    words.append(s)
    trimwords.append(s.strip())

# OK show words output with padding
for word in words:
    print word

# Build a list of letters 
for word in words:
    for c in word:
        if (c != " "):
            if not (c in letterlist):
                letterlist = letterlist + [c]

# Check we have no more than 10 letters
lettercount = len(letterlist)
if lettercount>10:
    print "Error! You have ",lettercount," letters => ",letterlist 
    quit()
else:
    print "Iterating :",letterlist

# Now Iterate through every possible digit selection
recurse_digits_combinations([],alldigits,lettercount-1)

# Put us onto a new line
sys.stdout.write('\n')

# Did we find a solution 
if not(solutioncount):
    print "Sorry, no solutions were found"
else:
    print "Found ",solutioncount, " solutions"
