"""
Challenge #7:

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).

Examples:
- nth_smallest([7, 5, 3, 1], 1) ➞ 1
- nth_smallest([1, 3, 5, 7], 3) ➞ 5
- nth_smallest([1, 3, 5, 7], 5) ➞ None
- nth_smallest([7, 3, 5, 1], 2) ➞ 3
"""


def nth_smallest(lst, n):
    # Your code here
    # create a variable to hold the value
    # sort the values
    # return the smallest in the given n
    # test to check if there is a number in the given n is higher than the lst length if not return None
    lst.sort()
    if n > len(lst):
        return "None"
    return lst[n - 1]


print(nth_smallest([7, 5, 3, 1], 1))
print(nth_smallest([1, 3, 5, 7], 3))
print(nth_smallest([1, 3, 5, 7], 5))
print(nth_smallest([7, 3, 5, 1], 2))
