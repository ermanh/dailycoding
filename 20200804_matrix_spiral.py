'''
2020-08-04
[from dailycodingproblem.com #65]

Given a N by M matrix of numbers, return a list of the elements in the matrix 
in a clockwise spiral.

For example, given the following matrix:

    [[1,  2,  3,  4,  5],
     [6,  7,  8,  9,  10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20]]

You should return:

    [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

'''

def matrix_spiral(N, M):
    if N <= 0 or M <= 0:
        return []

    matrix = [[num for num in range(i, i + M)] 
              for i in range(1, N * M + 1, M)]
    
    row = [0, N-1]
    column = [0, M-1]
    reverse = False
    print_order = []

    while column[1] + 1 > column[0] or row[1] + 1 > row[0]:
        if reverse is False:
            for j in range(column[0], column[1] + 1):
                print_order.append(matrix[row[0]][j])
            row[0] += 1

            for i in range(row[0], row[1] + 1):
                print_order.append(matrix[i][column[1]])
            column[1] -= 1
        else:
            for j in range(column[1], column[0] - 1, -1):
                print_order.append(matrix[row[1]][j])
            row[1] -= 1
            
            for i in range(row[1], row[0] - 1, -1):
                print_order.append(matrix[i][column[0]])
            column[0] += 1
            
        reverse = not reverse
        
    return print_order[:N * M]


'''
# TESTS
matrix_spiral(4, 5) == [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 
                        6, 7, 8, 9, 14, 13, 12]
matrix_spiral(4, 4) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
matrix_spiral(4, 3) == [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
matrix_spiral(3, 3) == [1, 2, 3, 6, 9, 8, 7, 4, 5] 
matrix_spiral(3, 2) == [1, 2, 4, 6, 5, 3] 
matrix_spiral(2, 3) == [1, 2, 3, 6, 5, 4] 
matrix_spiral(2, 2) == [1, 2, 4, 3] 
matrix_spiral(2, 1) == [1, 2] 
matrix_spiral(1, 1) == [1]
matrix_spiral(1, 0) == [] 
matrix_spiral(-1, -1) == [] 
'''
