"""
Write a Python program to input marks for five subjects
Physics, Chemistry, Biology, Mathematics, and Computer.
Calculate the percentage and grade according to the following:
Percentage >= 90% : Grade A Percentage >= 80% : Grade B Percentage >= 70% :
Grade C Percentage >= 60% : Grade D Percentage >= 40% : Grade E Percentage < 40% : Grade F
"""
grades = {}
grades['physics'] = input("What've you got in Physics? ")
grades['chemistry'] = input("What've you got in Chemistry? ")
grades['biology'] = input("What've you got in Biology? ")
grades['math'] = input("What've you got in Mathematics? ")
grades['computer'] = input("What've you got in Computer? ")


def grade(subject):
    mark_num = float(grades[subject])
    if mark_num >= 90:
        return f'Your grade in {subject} is: A'
    elif mark_num >= 80:
        return f'Your grade in {subject} is: B'
    elif mark_num >= 70:
        return f'Your grade in {subject} is: C'
    elif mark_num >= 60:
        return f'Your grade in {subject} is: D'
    elif mark_num >= 40:
        return f'Your grade in {subject} is: E'
    elif mark_num < 40:
        return f'Your grade in {subject} is: F'


for i in grades.keys():
    print(grade(i))
