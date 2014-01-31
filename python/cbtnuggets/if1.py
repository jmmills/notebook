#!/usr/bin/python

yn = input("Continue? Yes or No: ")
yn = yn.lower()

if yn[0] == 'y':
    print ("You typed 'Yes.'\n")
elif yn[0] == 'n':
    print ("You typed 'No.'\n")
elif yn == 'spam':
    print ("What are you doing?\n")
else:
    print ("You entered an invalid response.")
