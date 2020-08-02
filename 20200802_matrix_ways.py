'''
2020-08-02
[from dailycodingproblem.com #62]

There is an N by M matrix of zeroes. Given N and M, write a function to count 
the number of ways of starting at the top-left corner and getting to the 
bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two 
ways to get to the bottom-right:

Right, then down
Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
'''

def matrix_ways(N, M, n=0, m=0, counts=0):
    if 1 in [N, M]:
        return 1

    if n == N - 1 and m == M - 1:
        return counts

    if n + 1 < N and m + 1 < M:
        return matrix_ways(N, M, n + 1, m, 1) + matrix_ways(N, M, n, m + 1, 1)
    
    if n + 1 < N and m == M - 1:
        return matrix_ways(N, M, n + 1, m, counts)
    
    if m + 1 < M and n == N - 1:
        return matrix_ways(N, M, n, m + 1, counts)


'''
# TESTS

matrix_ways(1, 1) == 0
matrix_ways(2, 1) == 1
matrix_ways(2, 2) == 2
matrix_ways(2, 3) == 3
matrix_ways(2, 4) == 4
matrix_ways(3, 3) == 6
matrix_ways(3, 4) == 10
matrix_ways(3, 5) == 15
matrix_ways(4, 4) == 20
matrix_ways(4, 5) == 35
matrix_ways(5, 5) == 70
'''
