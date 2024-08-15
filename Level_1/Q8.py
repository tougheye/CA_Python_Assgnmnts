"""
Write a Python program to calculate the LCM (Least Common Multiple) of two numbers.
number1 = 12, number2 = 18 LCM of 12 and 18 are: 36
"""

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))


def find_lcm(num1, num2):
    smaller = min(num1, num2)           # first find the smaller of the 2 number
    common_factors = []                 # save the common factors in a list

    for i in range(1, smaller + 1):     # run the loop up to hte smaller number
        if num1 % i == 0 and num2 % i == 0:         # filter out the common factors and save in the list
            common_factors.append(i)

    LCM = (num1 * num2) / max(common_factors)           # calculate the LCM using definition
    return f'LCM of {num1} and {num2} is: {int(LCM)}'

print(find_lcm(number2, number1))

