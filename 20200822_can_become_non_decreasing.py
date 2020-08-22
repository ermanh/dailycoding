'''
2020-08-22
[from dailycodingproblem.com #79]

Given an array of integers, write a function to determine whether the array 
could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can 
modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any 
one element to get a non-decreasing array.
'''

def can_become_non_decreasing(array):
    decreases = 0
    for i, num in enumerate(array[1:], start=1):
        if array[i - 1] > num:
            decreases += 1
            array[i - 1] = num
            if i + 1 < len(array) and i - 1 > 0:
                for j in range(i + 1):
                    if array[j] > array[i + 1] or array[j] > num:
                        return False
            
    if decreases <= 1:
        return True
    return False


'''
# TESTS
can_become_non_decreasing([10, 5, 7]) == True
can_become_non_decreasing([10, 5, 1]) == False
can_become_non_decreasing([1, 5, 7]) == True
can_become_non_decreasing([5, 5, 7]) == True
can_become_non_decreasing([5, 5, 1]) == True
can_become_non_decreasing([5, 5, 5]) == True

can_become_non_decreasing([10, 5, 7, 10]) == True
can_become_non_decreasing([1, 10, 5, 7, 10]) == True
can_become_non_decreasing([7, 7, 5, 5]) == False
can_become_non_decreasing([1, 2, 10, 5, 7, 4]) == False
can_become_non_decreasing([1, 2, 10, 5, 8, 9]) == True
can_become_non_decreasing([5, 5, 5, 8, 6, 6]) == True
can_become_non_decreasing([5, 5, 5, 8, 4, 6]) == False
can_become_non_decreasing([5, 5, 5, 8, 7, 6]) == False
can_become_non_decreasing([5, 5, 5, 6, 7, 6]) == True
can_become_non_decreasing([5, 4, 5, 6, 7, 6]) == False
'''
    
