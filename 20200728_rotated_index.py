'''
2020-07-28
[from dailycodingproblem.com #58]

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster 
than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, 
return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
'''

# COMMENTS
# This solution requires O(n/2 + 1) time in the worse case scenario.
# It checks only every other index, and compares them to the element whose 
# index is desired.
# The last values lower/larger than the desired element, and their indices, 
# are continually updated to help determine whether the desired element is 
# between two neighboring checked indices


def rotated_index(array, elem):

    # Values initialized to -1 or elem to avoid clumsy None checking
    last_lower = -1
    last_lower_value = elem
    last_larger = -1
    last_larger_value = elem

    for i in range(0, len(array), 2):
        num = array[i]

        if num == elem:
            return i
        
        elif num < elem:
            if i - last_lower == 2 and num < last_lower_value:
                # If elem is largest in array
                return i - 1
            last_lower = i
            last_lower_value = num
        
        elif num > elem:
            if i - last_lower == 2:
                # If elem is in order between neighboring numbers
                return i - 1
            if last_larger_value > num and i - last_larger == 2:
                # If elem is smallest in array
                return i - 1
            if last_larger_value < num:
                last_larger = i
                last_larger_value = num

    return len(array) - 1


'''
# TESTS

rotated_index([8, 10, 13, 18, 25, 2], 8) == 0
rotated_index([2, 8, 10, 13, 18, 25], 8) == 1
rotated_index([25, 2, 8, 10, 13, 18], 8) == 2
rotated_index([18, 25, 2, 8, 10, 13], 8) == 3
rotated_index([13, 18, 25, 2, 8, 10], 8) == 4
rotated_index([10, 13, 18, 25, 2, 8], 8) == 5

# Desired element is smallest element
rotated_index([2, 8, 10, 13, 18, 25], 2) == 0
rotated_index([25, 2, 8, 10, 13, 18], 2) == 1
rotated_index([18, 25, 2, 8, 10, 13], 2) == 2
rotated_index([13, 18, 25, 2, 8, 10], 2) == 3
rotated_index([10, 13, 18, 25, 2, 8], 2) == 4
rotated_index([8, 10, 13, 18, 25, 2], 2) == 5

# Desired element is largest element
rotated_index([25, 2, 8, 10, 13, 18], 25) == 0
rotated_index([18, 25, 2, 8, 10, 13], 25) == 1
rotated_index([13, 18, 25, 2, 8, 10], 25) == 2
rotated_index([10, 13, 18, 25, 2, 8], 25) == 3
rotated_index([8, 10, 13, 18, 25, 2], 25) == 4
rotated_index([2, 8, 10, 13, 18, 25], 25) == 5
'''
