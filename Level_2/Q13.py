"""
Write a Python program to find if a given string starts with a given character using Lambda.
Sample input: input_string = "Hello, World!", given_char = "H" Sample Output: True
"""


user_input = input('Please enter the string: ')
character = 'H'


def check_first_letter(input_str, char):
    return (lambda input_str, char : input_str[0] == char)(input_str, char)


print(check_first_letter(user_input,character))

