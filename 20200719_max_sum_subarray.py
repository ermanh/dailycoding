'''
2020-07-19
[from dailycodingproblem.com #49]

Given an array of numbers, find the maximum sum of any contiguous subarray of 
the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would 
be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would 
not take any elements.

Do this in O(N) time.
'''


def max_sum_subarray(array):
    for i, current in enumerate(array[1:], start=1):
        if array[i - 1] > 0:
            array[i] = current + array[i - 1]
    return max(array) if max(array) > 0 else 0


'''
# TESTS

max_sum_subarray([34, -50, 42, 14, -5, 86]) == 137
max_sum_subarray([34, -50, 42, 14, -5, -1]) == 56
max_sum_subarray([34, -20, 42, 14, -5, -1]) == 70
max_sum_subarray([-5, -1, -8, -9]) == 0
max_sum_subarray([-5, -1, -8, 10]) == 10
max_sum_subarray([2, -1, 2, -9]) == 3
'''


        
