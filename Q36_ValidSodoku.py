class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:  # Return a boolean; write 4 other functions for clearer structures
        return (self.is_row_valid(board) and
                self.is_col_valid(board) and
                self.is_square_valid(board))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        # The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
        # '*': The * operator unpacks arguments in a function invocation statement. https://stackoverflow.com/questions/29139350/difference-between-ziplist-and-ziplist/29139473#29139473
        for col in zip(*board):  # '*board' is essentially disintegrating the matrix into its columns
            if not self.is_unit_valid(col):
                return False
        return True

    def is_square_valid(self, board):
        for i in (0, 3, 6):  # note the indices
            for j in (0, 3, 6):  # note the indices
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]  # nested for loops in list comprehension
                if not self.is_unit_valid(square):
                    return False
        return True

    def is_unit_valid(self, unit):  # validity-check function
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)  # !!!: genius! use 'set' to remove duplicates, instead of checking one by one
