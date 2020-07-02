'''
2020-07-02
[from dailycodingproblem.com]

You are given an array of non-negative integers that represents a 
two-dimensional elevation map where each element is unit-width wall and the 
integer is the height. Suppose it will rain and all spots between two walls 
get filled up.

Compute how many units of water remain trapped on the map in O(N) time and 
O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the 
middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 
2 in the second, and 3 in the fourth index (we cannot hold 5 since it would 
run off to the left), so we can trap 8 units of water.
'''

def water_trapped(array):
    trapped = [0 for _ in array]
    before_wall_index = 0

    for i, elem in enumerate(array[1:-1], start=1):    
        before_wall = array[before_wall_index]
        before = array[i-1]
        after = array[i+1]
        higher_before = max([before_wall, before])

        if elem > higher_before:
            before_wall_index = i

        if elem < min([higher_before, after]):
            trapped[i] = min([higher_before, after]) - elem
        
        if after >= max([elem, higher_before]):
            for j in range(before_wall_index + 1, i + 1):
                trapped[j] = higher_before - array[j] 

    return sum(trapped)


'''
# TESTS (all must return True)

# Walls at the edges (and middle)
water_trapped([3, 0, 1, 3, 0, 5]) == 8
water_trapped([3, 0, 1, 1, 0, 1]) == 2
water_trapped([4, 0, 1, 1, 0, 5]) == 14

# Walls not at the edges
water_trapped([0, 3, 2, 0, 3, 0]) == 4
water_trapped([0, 1, 4, 2, 3, 0]) == 1

# One edge wall and one middle wall
water_trapped([8, 1, 2, 9, 3, 2]) == 13
water_trapped([0, 1, 2, 9, 3, 6]) == 3

# No wells
water_trapped([0, 1, 4, 2, 1, 0]) == 0
water_trapped([9, 8, 7, 6, 5, 4]) == 0
water_trapped([0, 1, 2, 3, 4, 5]) == 0
water_trapped([1, 1, 1, 1, 1, 1]) == 0
'''
