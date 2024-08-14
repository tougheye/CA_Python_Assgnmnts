"""Read the doc.txt file using Python File handling concept and
return only the even length string from the file.
Consider the content of doc.txt as given below:
Hello I am a file
Where you need to return the data string which is of even length.
Make sure you return the content in The same link as it is present."""


# Creating and writing to a .txt file
with open('doc.txt', 'w') as file:
    file.write("Hello I am a file\n")


# reading the line from the file to subsequently parse
def read_even_strs(file_path):
    with open(file_path, 'r') as file:              # write the file to do operations
        line = file.read()
        line_list = line.split()

    with open(file_path, 'a') as file:          # append the even length strings to the file
        for i in line_list:
            if len(i) % 2 == 0:
                file.write(f'{i}\n')


read_even_strs('doc.txt')