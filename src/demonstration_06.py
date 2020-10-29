"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False

# set an o and x counter to zero
# Loop over each character in the string
# do a check if it contains an x
# increment x counter
# do a check if it contains an o
# increment o counter
# check if x counter is equal to o counter
# otherwise return false
"""


# def XO(txt):
# Your code here
# o_counter = 0
# x_counter = 0
# for char in txt:
#     if char == "o" or char == "O":
#         x_counter += 1
#     elif char == "x" or char == "X":
#         o_counter += 1

# if x_counter == o_counter:
#     return True
# else:
#     return False

def XO(txt: str) -> bool:
    lower_txt = txt.lower()
    return lower_txt.count("x") == lower_txt.count("o")


print(XO("xxoo"))
print(XO("xoxoo"))
