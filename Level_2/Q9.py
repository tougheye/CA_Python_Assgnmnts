"""
Write a Python program that executes an operation on a list
and handles an IndexError exception if the index is out of range.
"""

def ind_err(list1):
    result = []
    try:
        for i in range(len(list1)):
            result.append(list1[i + 1])     # should throw an Index error
    except IndexError:
        return 'OOPS! index out of range'
    return result


my_list = [2, 2, 5, 4, 9]

print(ind_err(my_list))