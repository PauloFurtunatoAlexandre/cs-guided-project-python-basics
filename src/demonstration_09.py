"""
Challenge #9:

Write a function that creates a dictionary with each (key, value) pair being
the (lower case, upper case) versions of a letter, respectively.

Examples:
- mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
- mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
- mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

Notes:
- All of the letters in the input list will always be lowercase.
"""


def mapping(letters):
    # Your code here
    # need to loop through all elements in the letters
    # create a key and value based on the letter index of letters
    # the key in the input will be lowercase
    # the value in the input will be lowercase
    # convert items to string
    new_dictionary = dict(zip(letters, [l.upper() for l in letters ]))
    return new_dictionary


print(mapping(["p", "s"]))
print(mapping(["a", "b", "c"]))
print(mapping(["a", "v", "y", "z"]))
