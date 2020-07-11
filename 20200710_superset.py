'''
The power set of a set is the set of all its subsets. Write a function that, 
given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return 
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
'''

from itertools import combinations


def powerset(regular_set):
    set_list = list(set(regular_set))
    greater_set = []
    for i in range(len(set_list) + 1):
        combos = combinations(set_list, i)
        for combo in combos:
            greater_set.append(list(combo))
    return greater_set


'''
# TESTS
powerset({}) == [[]]
powerset({1}) == [[], [1]]
powerset({2, 3}) == [[], [2], [3], [2, 3]]
powerset({1, 2, 3}) == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
powerset({4, 5, 6, 7}) == [
    [], [4], [5], [6], [7], [4, 5], [4, 6], [4, 7], [5, 6], [5, 7], [6, 7], 
    [4, 5, 6], [4, 5, 7], [4, 6, 7], [5, 6, 7], [4, 5, 6, 7]
]
powerset({2, 4, 6, 8, 10}) == [
    [], [2], [4], [6], [8], [10], [2, 4], [2, 6], [2, 8], [2, 10], [4, 6], 
    [4, 8], [4, 10], [6, 8], [6, 10], [8, 10], [2, 4, 6], [2, 4, 8], 
    [2, 4, 10], [2, 6, 8], [2, 6, 10], [2, 8, 10], [4, 6, 8], [4, 6, 10], 
    [4, 8, 10], [6, 8, 10], [2, 4, 6, 8], [2, 4, 6, 10], [2, 4, 8, 10], 
    [2, 6, 8, 10], [4, 6, 8, 10], [2, 4, 6, 8, 10]
] 

# Passing a set or array with repeated items should not result in duplicates
powerset({1, 1, 1}) == [[], [1]]
powerset([1, 1, 1]) == [[], [1]]
'''
