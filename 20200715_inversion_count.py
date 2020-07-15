'''
2020-07-15
[from dailycodingproblems.com #44]

We can determine how "out of order" an array A is by counting the number of 
inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] 
but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than 
O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has 
three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has 
ten inversions: every distinct pair forms an inversion.
'''

# Solution comments: 
# Used merge sort to perform recursive comparisons between elements in the 
# right array with elements in the left array, with O(n log n) performance


class Inversions:

    def __init__(self, array):
        self.array = array
        self.counts = 0
        self.result = self.merge_sort(self.array)

    def count(self):
        return self.counts

    def merge_sort(self, array):
        if len(array) < 2:
            return array

        result = []
        midpoint = int(len(array) / 2)
        left = self.merge_sort(array[:midpoint])
        right = self.merge_sort(array[midpoint:])

        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(right[j])
                j += 1
                self.counts += (len(left) - i) 
            else:
                result.append(left[i])
                i += 1 

        result += left[i:]
        result += right[j:]
        return result


'''
# TESTS
Inversions([1, 2, 3, 4, 5]).count() == 0
Inversions([2, 1, 3, 4, 5]).count() == 1
Inversions([2, 1, 4, 3, 5]).count() == 2
Inversions([2, 4, 1, 3, 5]).count() == 3
Inversions([3, 2, 1, 5, 4]).count() == 4
Inversions([2, 3, 5, 4, 1]).count() == 5
Inversions([4, 2, 5, 1, 3]).count() == 6
Inversions([4, 5, 2, 1, 3]).count() == 7
Inversions([4, 5, 2, 3, 1]).count() == 8
Inversions([4, 5, 3, 2, 1]).count() == 9
Inversions([5, 4, 3, 2, 1]).count() == 10
'''



