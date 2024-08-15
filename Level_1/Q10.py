"""
Write a Python program to reverse the order of words in a given sentence.
Input_sentence = “Hello, World! Welcome to Python programming.”
Output after reverse = “programming. Python to Welcome World! Hello,”
"""

input_string = input('Please enter your string: ')


def reverse_str(string1):
    # the function will split the string into individual words based on empty spaces
    # then join the list in the reverse order
    words = string1.split()
    print(f'Output after reverse = {" ".join(words[::-1])}')


reverse_str(input_string)



