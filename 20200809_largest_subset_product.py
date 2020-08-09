'''
2020-08-09
[from dailycodingproblem.com #69]

Given a list of integers, return the largest product that can be made by 
multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, 
since that's -10 * -10 * 5.

You can assume the list has at least three integers.
'''

from itertools import combinations
from functools import reduce

def largest_product(array):
    products = []
    for c in combinations(array, 3):
        product = reduce(lambda a, b: a * b, c)
        products.append(product)
    return max(products)


'''
# TESTS

largest_product([-10, -10, 5, 2]) == 500
largest_product([-10, 10, 5, 2]) == 100
largest_product([-10, -10, -10, -10]) == -1000
largest_product([3, 4, 5, 2]) == 60
'''
