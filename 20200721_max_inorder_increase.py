'''
2020-07-21
[from dailycodingproblem.com #47]

Given a array of numbers representing the stock prices of a company in 
chronological order, write a function that calculates the maximum profit you 
could have made from buying and selling that stock once. You must buy before 
you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could 
buy the stock at 5 dollars and sell it at 10 dollars.
'''

def max_inorder_increase(array):
    profit = max(array[1:]) - array[0]
    for i, num in enumerate(array[1:-1], start=1):
        largest_increase = max(array[i+1:]) - num
        if largest_increase > profit:
            profit = largest_increase
    return profit if profit > 0 else 0


'''
# TESTS

max_inorder_increase([9, 11, 8, 5, 7, 10]) == 5
max_inorder_increase([1, 11, 8, 5, 7, 10]) == 10
max_inorder_increase([40, 11, 8, 2, 7, 10]) == 8

# No increase should return 0
max_inorder_increase([11, 10, 9, 8, 7, 6]) == 0
max_inorder_increase([11, 9, 7, 5, 4, 2]) == 0
max_inorder_increase([2, 2, 2, 2, 2, 2]) == 0
'''
