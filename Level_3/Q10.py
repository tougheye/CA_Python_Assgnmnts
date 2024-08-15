"""A cafe has N computers. Several customers come to the cafe to use these computers.
A customer will be serviced only if there is any unoccupied computer at the moment
the customer visits the cafe. If there is no unoccupied computer, the customer leaves the cafe.
You are given an integer N representing the number of computers in the cafe and
a sequence of uppercase letters S. Every letter in S occurs exactly two times.
The first occurrence denotes the arrival of a customer and the second occurrence denotes
the departure of the same customer if he gets allocated the computer.
You have to find the number of customers that walked away without using a computer."""


def num_cust_cant_use_comp(sequence, comp_cnt):
    occupied_comp_count = 0
    current_users = set()
    stand_by_user = set()
    user_walked_away = []

    for char in sequence:  # if there is any available computer
        if char not in current_users.union(stand_by_user):  # if computer available, new customer would use it
            if occupied_comp_count < comp_cnt:
                current_users.add(char)
                occupied_comp_count += 1
            else:  # if computer is not available, new customer would be standby
                stand_by_user.add(char)
        elif char in current_users:  # the user leaving
            current_users.remove(char)
            occupied_comp_count -= 1
        elif char in stand_by_user:  # a standby customer leaving
            stand_by_user.remove(char)
            user_walked_away.append(char)

    return f'{user_walked_away} will not be able to get any computers. So the answer is {len(user_walked_away)}.'

print(num_cust_cant_use_comp('ABCBAC',1))
