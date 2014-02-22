#!/usr/bin/env python

__author__ = 'jason'

'''
Name: modtest.py
Author: Jason M. Mills
Purpose: test out module imports
'''


def square(x):
    # returns square of given integer
    return x * x

if __name__ == '__main__':
    print('Testing: square of 2 == ', square(2))
