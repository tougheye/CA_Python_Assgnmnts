"""
Write a Python program to find if a given string starts with a given character
using Lambda.
Sample input: input_string = "Hello, World!", given_char = "H" Sample Output: True
"""


user_input = input('Please enter the string: ')
character = input('Enter the Character (case sensitive): ')


def check_first_letter(input_str, char):
    # Define and call the lambda function
    return (lambda input_str, char : input_str[0] == char)(input_str, char)


print(f'Does {user_input} start with {character}? {check_first_letter(user_input,character)}')

