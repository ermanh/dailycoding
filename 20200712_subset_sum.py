'''
Work In Progress
[from dailycodingproblem.com #42]

Given a list of integers S and a target number k, write a function that 
returns a subset of S that adds up to k. If such a subset cannot be made, then 
return null.

Integers can appear more than once in the list. You may assume all numbers in 
the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] 
since it sums up to 24.
'''

from itertools import combinations


def subset_sum(array, k):
    less_than = sorted([num for num in array if num <= k], reverse=True)
    for i in range(1, len(less_than) + 1):
        for c in combinations(less_than, i):
            if sum(c) == k:
                return list(c)
    return None


'''
# TESTS (should all return true)

subset_sum([12, 1, 61, 5, 9, 2], 24) == [12, 9, 2, 1]
subset_sum([12, 1, 61, 5, 9, 24], 24) == [24]
subset_sum([12, 1, 61, 5, 9, 24], 36) == [24, 12]
subset_sum([3, 6, 12, 7, 4, 23], 55) == [23, 12, 7, 6, 4, 3]
subset_sum([3, 6, 12, 7, 4, 23], 57) == None
subset_sum([3, 6, 12, 7, 4, 23, 25], 73) == [25, 23, 12, 7, 6]
subset_sum([1, 1, 2, 2, 3, 3], 12) == [3, 3, 2, 2, 1, 1]
subset_sum([1, 1, 2, 2, 3, 3], 10) == [3, 3, 2, 2]
subset_sum([1, 1, 2, 2, 3, 3], 4) == [3, 1]
'''
