'''
Title: Guess the Numbers game
Adapted from: inventwithpython.com
Purpose: Demo a live Python program
'''

import random

guessesTaken = 0

print ('Hello! What is your name?')
myName = input()

number = random.randint (1, 20)
print ('Well, ' + myName + ', I am thinking of a number between 1 and 20. What is it?')

while guessesTaken < 6:
    guess = int( input('Take a guess? ') )
    guessesTaken += 1

    if guess < number:
        print ('Your guess is too low.')

    if guess > number:
        print ('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print ('Good job, ' + myName + '! you guessed my number in ' + guessesTaken + ' guesses!')
else:
    print ('You failed to guess my number')
    
    
