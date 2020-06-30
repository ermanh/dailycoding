'''
2020-06-03
[from www.dailycodingproblem.com]

Given an array of integers, return a new array such that each element at index 
i of the new array is the product of all the numbers in the original array 
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would 
be [2, 3, 6].

Follow-up: what if you can't use division?
'''

from functools import reduce


def product_list(lst):
    new_list = []

    for i, _ in enumerate(lst):
        temp_list = list(lst)
        temp_list.pop(i)
        new_list += [reduce(lambda a, b: a*b, temp_list)]

    return new_list


'''
# Tests (should all return True)

product_list([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
product_list([3, 2, 1]) == [2, 3, 6]
'''
