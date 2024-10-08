"""
Create a login page backend to ask users to enter the username and password.
Make sure to ask for a Re-Type Password and if the password is incorrect
give a chance to enter it again but it should not be more than 3 times.
"""

username = input("Please input your username: ")

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Please enter your password: ")
    retype_password = input("Please re-type your password: ")

    # if the passwords match, let the user in
    if password == retype_password:
        print("Perfect! You are in!")
        break
    # if the retyped passwords don't match, increase the attempt count and show message
    else:
        attempts += 1
        print(f"Password do not match. Please try again. ({max_attempts - attempts} attempts left)")

# if the user uses up all 3 attempts
if attempts == max_attempts:
    print("Sorry! You have no more attempts left")

