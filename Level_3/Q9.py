"""
Given an input string, write a function that returns the run length encoded string for the input string.
For Example:
Input: wwwwaaadebbbbbw Output: w4a3d1e1b5w1
"""

inp_str = 'wwwwaaadebbbbbw'


def len_encod_str(input_str):
    output_str = input_str[0]           # starting the new output string with the first letter of the input string
    # due to the nature of the for loop below
    cur_str_cnt = 1                 # since the output string will always have at least 1 character, in case for the
    # new string, it will be counted within the for loop

    # the for loop will iterate through the input string
    for i in input_str[1:]:
        # if the next str is the same as the last string,
        # it only counts up,
        if i == output_str[-1]:
            cur_str_cnt += 1
        # otherwise, it adds the count of the current str in the output string and then adds the count number
        else:
            output_str = output_str + f'{cur_str_cnt}{i}'
            cur_str_cnt = 1

    return output_str + str(cur_str_cnt)  # need to add the count of the final character separately

print(len_encod_str(inp_str))
