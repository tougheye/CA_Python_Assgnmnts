"""
Write a program that accepts a string as input from the user and calculates the number of digits and letters.
Input: Hello123
Output: Alphabets: 5 & Number : 3
"""

def calc_num_alp():
    str_input = input('Please enter your string: ')
    alphabets = 0
    number = 0
    for i in str_input:
        if i.isnumeric():
            number += 1
        elif i.isalpha():
            alphabets += 1
        else:
            continue

    return f'Alphabest: {alphabets} & Number: {number}'

print(calc_num_alp())