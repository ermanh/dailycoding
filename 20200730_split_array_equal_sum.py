'''
2020-07-30
[from dailycodingproblem.com #60]

Given a multiset of integers, return whether it can be partitioned into two 
subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return 
true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which 
both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't 
split it up into two subsets that add up to the same sum.
'''

# SOLUTION COMMENT
# Assuming one subset includes the largest and smallest elements in the array, 
# then almost all elements require going through the for loop twice (for all 
# elements in between, once appending to and once popping from half_array; 
# for the last element, once appending to half_array, and one last time 
# checking the sum), hence range(len(array) * 2 - 1) in the for loop


def equal_sum_subarrays(array):
    if sum(array) % 2 != 0:
        return False
    
    half_amount = int(sum(array) / 2)
    array = sorted(array, reverse=True)
    half_array = []
    for _ in range(len(array) * 2 - 1):
        if sum(half_array) == half_amount:
            return True
        elif sum(half_array) > half_amount:
            array.append(half_array.pop())
        else:
            half_array.append(array.pop(0))

    return False


'''
# TESTS

equal_sum_subarrays([15, 5, 20, 10, 35, 15, 10]) == True
equal_sum_subarrays([15, 5, 20, 10, 35]) == False

equal_sum_subarrays([1, 2, 2, 3]) == True  # [3, 1], [2, 2]
equal_sum_subarrays([1, 2, 2, 5]) == True  # [5], [2, 2, 1]
equal_sum_subarrays([1, 2, 2, 7]) == False
equal_sum_subarrays([1, 3, 3, 7]) == True  # [7], [3, 3, 1]
equal_sum_subarrays([3, 3, 3, 7]) == False
equal_sum_subarrays([3, 5, 5, 7]) == True  # [7, 3], [5, 5]
equal_sum_subarrays([1, 1, 4, 5, 7]) == True  # [7, 1, 1], [5, 4]
equal_sum_subarrays([1, 1, 1, 2, 2, 2, 2, 2, 7]) == True  
    # [7, 2, 1], [2, 2, 2, 2, 1, 1]
'''



    
