"""
Write a Python program to create a list of given strings individually of the list
using the Python map function.
Eg. Input:
['Red', 'Blue', 'Black', 'White', 'Pink']
Output:
[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i',
'n', 'k']]
"""

input_list = ['Red', 'Blue', 'Black', 'White', 'Pink']

def indiv_str(input_str):
    return [i for i in input_str]

#the map function applies the predefined function on each list element
output_list = list(map(indiv_str, input_list))

print(output_list)