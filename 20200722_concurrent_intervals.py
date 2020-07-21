'''
2020-07-22
[from dailycodingproblem.com #21]

Given an array of time intervals (start, end) for classroom lectures 
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

def classrooms(array):
    rooms = 1
    for i, (a, b) in enumerate(array[:-1]):
        overlaps = 0
        for (c, d) in array[i+1:]:
            if a < c < b or a < d < b or c < a < d or c < b < d:
                overlaps += 1
        
        # if an interval overlaps with all remaining intervals to its right 
        # in the (sub)array, then an extra room is needed; else, it means it
        # can use the same classroom with at least one other interval 
        # without conflict
        if overlaps == len(array) - 1 - i:
            rooms += 1
    
    return rooms


'''
# TESTS

classrooms([(30, 75), (0, 20), (80, 150)]) == 1
classrooms([(30, 75), (0, 50), (60, 150)]) == 2
classrooms([(30, 75), (0, 70), (60, 150)]) == 3
classrooms([(30, 75), (0, 70), (60, 150), (20, 100)]) == 4
classrooms([(30, 75), (0, 70), (60, 150), (20, 100), (0, 40)]) == 4
classrooms([(30, 75), (0, 70), (60, 150), (20, 100), (0, 65)]) == 5
'''

