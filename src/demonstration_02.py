"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""
def convert(minutes:int):
    # Your code here
    # set seconds to the value of the expression minutes * 60
    # return seconds
    seconds = minutes * 60
    return seconds

print(convert(45))
print(convert(5))
print(convert(9))