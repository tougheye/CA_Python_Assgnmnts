"""
Write a Python program to find the common elements between two lists.
Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8] Sample output: [4, 5]
"""

l1 = [1, 2, 8, 4, 5]
l2 = [4, 5, 6, 7, 8]


def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return f'Sample output: {list(set1 & set2)}'


print(find_intersection(l1,l2))