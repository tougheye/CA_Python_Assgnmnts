"""
Given an array of size N. The task is to rotate array by D elements towards right
Sample Input: arr = [1, 2, 3, 4, 5], D = 2
Sample Output: arr after rotation = [4, 5, 1, 2, 3]
"""

arr = [1, 2, 3, 4, 5]


def switch_list_around(list1, d):
    len_list = len(list1)
    new_list = list1[len_list - d:]
    for i in range(len_list - d):
        new_list.append(list1[i])
    return new_list


print(switch_list_around(arr,2))
