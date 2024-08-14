"""Aditi has used text editing software to type some text.
After saving the article as words.txt, she realized that
she had wrongly typed the alphabet “J" instead of “I" everywhere in the article.
Write a function definition for JtoI() in Python that would display the corrected
version of the entire content of the file WORDS.TXT with all the alphabet "J" to be
displayed as an alphabet "I" on the screen.
Note: Assume that words.txt does not contain any J alphabet otherwise."""

# defining the function
def Jtol(file_path):
    with open(file_path,'r') as file:
        content = file.read()
        edited_content = content.replace('J', "I")
        edited_content = edited_content.replace("j", "i")

    with open(file_path, 'w') as file:
        file.write(edited_content)


# to prepare the initial .txt file, prepare the content
file_cont = "Jntelligence js key to success, " \
            "but jnterest and passjon jn your work are equally " \
            "jmportant for achjeving great results."

# write the content string in the .txt file
with open('words.txt', 'w') as file:
    file.write(file_cont)

# call the function
Jtol('words.txt')