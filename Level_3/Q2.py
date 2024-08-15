# Write a program to count the lines in a file “demo.txt”

def count_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open('demo.txt', 'w') as file:
        # the line count will be saved in demo.txt file
        file.write(f'"{file_path}" file has {len(lines)} lines')

count_line('doc.txt')

