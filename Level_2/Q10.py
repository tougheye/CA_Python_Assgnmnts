"""
We are making n stone piles! The first pile has n stones.
If n is even, then all piles have an even number of stones.
If n is odd, all piles have an odd number of stones.
Each pile must have more stones than the previous pile but as few as possible.
Write a Python program to find the number of stones in each pile.
"""


def pile_count(n):
    # since the first element is n itself, it only needs to increase in the increment of 2
    return [n + (i * 2) for i in range(n)]


print(pile_count(4))