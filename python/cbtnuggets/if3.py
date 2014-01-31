#!/usr/bin/python

forms = ['animal', 'mineral', 'vegetable']
answer = input("Are you animal, mineral, or vegetable? ")

if answer == forms[0]:
    print ("You are an animal. GRR!\n")
elif answer == forms[1]:
    print ("You are a mineral. You must be healthy.\n")
elif answer == forms[2]:
    print ("You are a vegetable. Do you do anything at all!\n")
else:
    print ("You did not give a valid response.\n")
