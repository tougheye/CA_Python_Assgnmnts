"""
Write a Python program to find the sum of all odd numbers between two given numbers.
Start = 1, stop = 10
Sum of odd numbers: 25
"""

start_num = int(input('Please enter the start integer: '))
stop_num = int(input("Please enter the stop integer: "))


def sum_of_odd(start, stop):
    sum_odd = 0
    for i in range(start, stop+1):
        if i % 2 != 0:      # filter if the number is odd
            sum_odd += i
    return f'The sum of the odd numbers in this range is {sum_odd}'

print(sum_of_odd(start=start_num,stop=stop_num))
