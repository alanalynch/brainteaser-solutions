#!/usr/bin/python

def isPalindrome(string):
    testStr = str(string).lower().replace(" ","") # in case it's a number or something funky, then lowercase it, then rid the world of spaces
    begin = 0
    end = len(testStr) - 1 # this is not Pythonic but using negative indices makes the code borderline unreadable

    while begin < end:
        if testStr[begin] != testStr[end]:
            return False

        begin = begin + 1
        end = end - 1

    return True
