"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one == list_two:
        return 3
    smaller, bigger, result = (
        (list_two, list_one, 2)
        if len(list_two) < len(list_one)
        else (list_one, list_two, 1)
    )
    for r in range(len(bigger)):
        if smaller == bigger[r : (r + len(smaller))]:
            return result
    return 4
