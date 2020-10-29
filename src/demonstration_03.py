"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt):
    # Your code here
    # return the txt as int by using the int() constructor to convert it to an Integer
    number = int(txt)
    return number

print(string_int("6"))
print(string_int("1000"))
print(string_int("12"))