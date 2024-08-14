"""
Write a Python program to calculate the sum of digits of a given number until the sum becomes a single-digit number.
Sample Input: num = 987
Sample Output: Sum_of_digits = 24,
Again compute the sum of digits so that it can be reduced to on single digit.
Final Output: 6
"""

input_num = input('Enter a number: ')

# Create a function to calculate the sum of the digits in the string
def calc_sum_of_digits(input_num):
    nums = list(input_num)
    sum_of_digit = 0
    for num in nums:
        sum_of_digit += int(num)
    return sum_of_digit


# function to take in a number and spit out a string
def int_to_str(num):
    return str(num)


def final_output(string_num):
    sum_digit = calc_sum_of_digits(string_num)

    while sum_digit > 9:
        sum_str = int_to_str(sum_digit)
        sum_digit = calc_sum_of_digits(sum_str)

    return f'Final Output: {sum_digit}'


print(final_output(input_num))









