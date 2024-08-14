"""You need to write a function that accepts an encoded string as a parameter.
This string will contain a first name, last name, and an id.
Values in the string can be separated by any number of zeros.
The id is a numeric value but will contain no zeros.
The function should parse the string and
return a Python dictionary that contains the first name, last name, and id values.
For example:
Input : “Robert000Smith000123”
Output:{ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }"""

input_str = 'Robert0000Smith0123'


# defining the function that will take the encoded string as input and return output dictionary paired with fields
def encode_parser(inp_str):
    field_names = ["first_name", "last_name", "id"]
    # using string's .split() to split the string where 0's occured. Since names can't have 0 and id values don't
    # take 0 in order to eleminate the empty strings created by .split(), we use the conditional boolean in the list
    # comprehension
    input_lst = [item for item in inp_str.split('0') if item]
    # dictionary comprehension to generate output dictionary
    output_dict = {key: value for key, value in
                   zip(field_names, input_lst)}
    return output_dict


print(encode_parser(input_str))
