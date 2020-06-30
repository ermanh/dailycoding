
'''
2020-06-09
[from dailycodingproblems.com]

Given a list of integers, write a function that returns the largest sum of 
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

(Following solution taken and translated from JavaScript: 
https://www.cnblogs.com/Answer1215/p/10554290.html)
'''


def largest_sum(array):
    max_increment = max(0, array[0])
    max_not_increment = max(array[1], max_increment)
    maximum = max_increment
    for i in range(2, len(array)):
        maximum = max(array[i] + max_increment, max_not_increment)
        max_increment = max_not_increment
        max_not_increment = maximum
    return maximum


'''
# Tests (should all return True)
largest_sum([2, 4, 6, 2, 5]) == 13
largest_sum([5, 1, 1, 5]) == 10
largest_sum([4, 2, -3, 2, 7, 3]) == 11
'''
