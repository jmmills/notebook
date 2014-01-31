#!/usr/bin/python

'''
This first unassigned string in a module
is the docstring!, What you see above
is an "exec/hack", that enables ilf1.py instead of python
if1.py in *NIX
'''

num = input("Enter an integer: ")
num = int(num)

if num < 0:
    print("The absolute value of", num, 'is', -num)
else:
    print("The absolute value of", num, 'is', num)

