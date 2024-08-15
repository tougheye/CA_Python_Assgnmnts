"""
Write a Python program to count the frequency of each element in a list.
Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5] Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
"""

Input_list = [1, 2, 2, 2, 4, 1, 2, 6, 5]

def freq_count(list1):
    output_dict = {}
    for i in list1:
        output_dict[i] = Input_list.count(i)        # dictionary key is the element in the list, value are the counts
    print(f'Frequency Count: {output_dict}')


freq_count(Input_list)