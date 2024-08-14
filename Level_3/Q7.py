"""Write a program to construct a dictionary from the two lists containing
the names of students and their corresponding subjects.
The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.
Input: [Sam, Alice, Mona] ,
[Commerce, Science, Computer]
Output: [Sam: Commerce, Alice: Science , Mona: Computer]"""

students = ['Sam', 'Alice', 'Mona']
subjects = ['Commerce', 'Science', 'Computer']

# dictionary using for loop
def dict_from_for(list1, list2):
    dict_for = {}

    for i in range(len(students)):
        dict_for[list1[i]] = list2[i]
    return dict_for

print(f'the dictionary using for loop is {dict_from_for(students,subjects)}')


# using dictionary comprehension
dict_comprehension = {key:value for key, value in zip(students,subjects)}
print(f'the dictionary using the comprehension method is {dict_comprehension}')