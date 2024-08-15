"""
Write a Python function that counts the number of vowels in a given string.
Sample Input: string = "Hello, World!" Sample Output: Number of vowels: 3
"""

input_string = input("String please: ")

def vowel_counter(string1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_cnt = 0

    for i in string1:
        if i.lower() in vowels:             #  check the lower case of each letter
            vowel_cnt += 1
    return f'Number of vowels: {vowel_cnt}'


print(vowel_counter(input_string))
