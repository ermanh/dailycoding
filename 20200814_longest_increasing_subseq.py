'''
2020-08-14
[from dailycodingproblem.com #75]

Given an array of numbers, find the length of the longest increasing 
subsequence in the array. The subsequence does not necessarily have to be 
contiguous.

E.g., given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''

def longest_increasing(array):
    sequences = []
    for i, num in enumerate(array):
        sequences.append([(i, num)])
        for sequence in sequences:
            if i > sequence[-1][0] and num > sequence[-1][1]:
                sequences.append(sequence + [(i, num)])

    sequences.sort(key=lambda x: len(x))
    sequences = [s for s in sequences if len(s) == len(sequences[-1])]

    if len(sequences[0]) == 1:
        return 0
    return len(sequences[0])


'''
# TESTS

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
longest_increasing(arr) == 6

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7]
longest_increasing(arr) == 5

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 3, 11, 7]
longest_increasing(arr) == 5

arr = [0, 8, 4, 12, 2, 10, 6, 14]
longest_increasing(arr) == 4

arr = [8, 4, 12, 2, 10, 6, 14]
longest_increasing(arr) == 3

arr = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11]
longest_increasing(arr) == 7

arr = [5, 4, 3, 2, 1]
longest_increasing(arr) == 0

arr = [5, 1, 5, 5, 6]
longest_increasing(arr) == 3
'''