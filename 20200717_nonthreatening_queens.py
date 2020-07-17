'''
2020-07-17
[from dailycodingproblem.com #38]

You have an N by N board. Write a function that, given N, returns the number 
of possible arrangements of the board where N queens can be placed on the 
board without threatening each other, i.e. no two queens share the same row, 
column, or diagonal.
'''


class NQueens:

    def __init__(self, N):
        self.N = N
        self.boards = None
        self.count = None
        self._get_arrangements()
    
    def _get_arrangements(self):
        empty_board = [['o' for _ in range(self.N)] for _ in range(self.N)]
        self.boards = self._populate_boards(0, [empty_board])
        self.count = len(self.boards)

    def _mark_conflicts(self, x, y, board):
        """Since rows are processed top to bottom, there's no need to mark 
        slots above row x.
        """
        directions = [
            zip((x for _ in range(self.N)), range(y)),  # left
            zip((x for _ in range(self.N)), range(y + 1, self.N)),  # right
            zip(range(x + 1, self.N), (y for _ in range(self.N))),  # down
            zip(range(x + 1, self.N), range(y - 1, -1, -1)),  # left-down
            zip(range(x + 1, self.N), range(y + 1, self.N))  # right-down
        ]
        new_board = [[elem for elem in row] for row in board]
        for direction in directions:
            for i, j in direction:
                new_board[i][j] = '_'
        return new_board
    
    def _populate_boards(self, row_index, boards):
        """Recursively generates and populates boards with non-conflicting 
        queens row by row.
        
        Since only one queen can be placed per row, this function only runs 
        N times recursively (but the number of boards may grow exponentially).
        """
        if row_index == self.N or len(boards) == 0:
            return boards
        
        new_boards = []
        for board in boards:
            for col_index in range(self.N):
                if board[row_index][col_index] != '_':
                    temp_board = [[elem for elem in row] for row in board]
                    temp_board[row_index][col_index] = 'Q'
                    new_board = self._mark_conflicts(
                        row_index, col_index, temp_board)
                    new_boards.append(new_board)

        return self._populate_boards(row_index + 1, new_boards)


'''
# TESTS

NQueens(0).count == 0
NQueens(1).count == 1
NQueens(2).count == 0
NQueens(3).count == 0
NQueens(4).count == 2
NQueens(5).count == 10
NQueens(6).count == 4
NQueens(7).count == 40
NQueens(8).count == 92
NQueens(9).count == 352
NQueens(10).count == 724
NQueens(11).count == 2680
NQueens(12).count == 14200
'''
