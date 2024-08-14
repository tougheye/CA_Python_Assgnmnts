"""
Write a Python program to calculate the LCM (Least Common Multiple) of two numbers.
number1 = 12, number2 = 18 LCM of 12 and 18 are: 36
"""

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))


def find_lcm(num1, num2):
    smaller = min(num1, num2)
    common_factors = []

    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_factors.append(i)

    LCM = (num1 * num2) / max(common_factors)
    return f'LCM of {num1} and {num2} is: {int(LCM)}'

print(find_lcm(number2, number1))

