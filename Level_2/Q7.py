"""
Write a Python function that finds the median of a list of numbers.
Sample Input: number_list = [7, 2, 5, 1, 9, 3] Sample Output: Median: 4.0
"""

def median_finder(num_list):
    sort_list = sorted(num_list)

    if len(num_list) % 2 == 0:      # median of the even length of list
        mid_low = len(num_list) / 2
        mid_high = mid_low + 1
        middle = (sort_list[mid_high] + sort_list[mid_low]) / 2         # using definition of median in even list
        return f'Median: {middle}'
    else:               # median for the odd length of list using floor division
        return f'Median: {sort_list[(len(num_list)//2)]}'


number_list = [7, 2, 5, 1, 9, 3, 3, ]

print(median_finder(number_list))


