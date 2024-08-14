"""
Write a Python program to reverse a number using a while loop.
Sample Input: num = 12345 Sample Output: revnum = 54321
"""

numbers = input('Enter the number: ')


def reverse_num(input_num):
    str_lst = list(input_num)
    reverse_str = ''

    while str_lst:
        next_digit = str_lst.pop()
        reverse_str = reverse_str + next_digit

    return f'Reverse number is {reverse_str}'


print(reverse_num(numbers))
