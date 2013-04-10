#!/usr/bin/env python
import re

"""
A simple exercise on detecting a palindrome.
"""
import sys


def reverse(text):
    return cleanse(text)[::-1]


def isPalindrome(text):
    return cleanse(text).lower() == reverse(text).lower()


def cleanse(text):
    return re.sub(r'[^A-Za-z]+', '', text)


if __name__ == '__main__':
    try :
        while (1) :
            text = raw_input("[Type exit to exit the program] or Enter text: ")
        
            if (text == 'exit') :
                sys.exit()
            elif (isPalindrome(text)):
                print("Yes, it is a palindrome")
            else:
                print("Nope, it is not a palindrome")
    except :
        print('\nprogram exiting')
        
