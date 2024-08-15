"""
Write a Python program to check if a number is a power of two using recursion.
"""

def power_of_two(n):

# base case - the lowest power of 2 is 1 = 2^0
    if n == 1:
        return True
# in recursion, if n < 1, that can't be a power of 2
    elif n < 1:
        return False
# the power of 2 has to be evenly divisible by 2 at all level which will return boolean
    else:
        return power_of_two(n // 2) and (n % 2 == 0)



print(power_of_two(8))
