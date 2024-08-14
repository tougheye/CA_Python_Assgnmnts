"""
Write a Python program to check if a given number is a perfect number.
A Perfect number is a positive integer that is equal to the sum of its proper divisors.
For instance, 6 has divisors 1, 2, and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number.
Input: 5 Output: No
"""

number = int(input("Enter the number: "))


def chk_perfect(num):
    divisors = []
    for i in range(1, (num//2)+1):          #since a number's largest divisor <= 1/2 of the number
        if num % i == 0:
            divisors.append(i)

    if sum(divisors) == num:
        return f'Input: {num} Output: Yes'
    else:
        return  f'Input: {num} Output: No'

print(chk_perfect(number))