"""
Write a Python program to check if a string is an anagram of another string.
string1 = "listen", string2 = "silent" Output: True
"""

from collections import Counter

string1 = input('Enter the 1st string: ')
string2 = input('Enter the 2nd string: ')

# python Counter function provides a dictionary whose keys are the
# elements of the iterable and the values are the count of the element in the
# iterable. Hence, if both dictionary are the same, the strings would be anagrams of each other
print(Counter(string1) == Counter(string2))
