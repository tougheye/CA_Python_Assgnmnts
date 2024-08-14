"""
Given an array of N integers and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
Sample Input: arr = [1, 2, 3, 4, 5], k = 6 Sample Output: Pair count: 2
"""


def pair_count(list1, k):
    cnt_pair = 0

    for i in range(len(list1)):
        remainder = k - list1[i]
        if remainder in list1[i + 1:]:
            cnt_pair += 1

    return f'Pair count: {cnt_pair}'

arr = [1, 6, 3, 4, 5, 8]

print(pair_count(arr, 9))