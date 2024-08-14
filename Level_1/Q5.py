"""
Write a Python program to find the factorial of a number using a for loop.
"""

target_num = int(input('Please enter your integer: '))

def factorial(num):
    fact = 1
    if num == 0 or num == 1:
        return f'The factorial for {num} is 1'
    else:
        for i in range(1, num+1):
            fact *= i
        return f'The factorial for {num} is {fact}'

print(factorial(target_num))