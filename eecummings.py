##
## formats everything into the style of an e.e. cummings poem.
##

## import random and text to speech

from random import randrange
import pyttsx

## text to turn into a poem
text = '''
The Dodge Custom Royal is an automobile which was produced by Dodge in the United States for the 1955 through 1959 model years. In each of these years the Custom Royal was the top trim level of the Dodge line, above the mid level Dodge Royal and the base level Dodge Coronet.
'''

## characters to randomly insert
fChar = ['\t', '\t(', ') ', '\n \t \t', '\n \t', '    ', ' ', ', ', ' ', ' ', ' ', '... ', '\n']

## split the text
t = text.split()

## make a function to return a number between 0 and the length of the 
def randPunct():
    return randrange(0,len(fChar))

## variables for changing variable types in the loops
b = {}
newT = {}
i = 0
newerT = []

## go through the split text, for each word pick a random formatting character from fChar 
for each in t:
    b[i] = fChar[randPunct()]
    newT[i] = each + b[i]
    i += 1

## loop again and put it in the right variable type
for each in newT:
	newerT += newT[each]

## put it all together
together = ''.join(newerT)

## print it out
print together

## use text to speech to say the text. helps to get an understand of the timing of the poem.
engine = pyttsx.init()
engine.say(together)
engine.runAndWait()
