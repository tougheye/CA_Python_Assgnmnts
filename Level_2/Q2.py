"""
Create a function that takes a list and returns a new list with unique elements of the first list.
Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5] Sample Output: list2 = [1, 2, 3, 4, 5]
"""


def unique_elem(input_list):
    list_set = set(input_list)
    return f'Sample Output: {list(list_set)}'


list1 = [1, 2, 2, 3, 4, 4, 5, 5]


print(unique_elem(list1))