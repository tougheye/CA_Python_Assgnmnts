"""
Create a login page backend to ask users to enter the username and password.
Make sure to ask for a Re-Type Password and if the password is incorrect
give a chance to enter it again but it should not be more than 3 times.
"""

input_uname = input('Please input your username: ')

attempt_cnt = 3

while attempt_cnt > 0:
    password = input('Please enter your password: ')
    retype_pw = input('Please re-type your password: ')

    if password == retype_pw:
        print("Perfect! You are in!")

    else:
        attempt_cnt -= 1
        if attempt_cnt > 0:
            retype_pw = input('Password do not match. Please re-type password: ')
        else:
            print('Sorry! You have no more attempt left')

