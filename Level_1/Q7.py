"""
Write a Python program to check if a string is an anagram of another string.
string1 = "listen", string2 = "silent" Output: True
"""

from collections import Counter

string1 = input('Enter the 1st string: ')
string2 = input('Enter the 2nd string: ')

print(Counter(string1) == Counter(string2))
