class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        " Q1314; integral image method "
        self.r, self.c = len(matrix), len(matrix[0])
        self.integral_mat = [[0 for _ in range(self.c)] for _ in range(self.r)]
        for i in range(self.r):
            sum = 0
            for j in range(self.c):
                sum += matrix[i][j]
                self.integral_mat[i][j] = sum
                if i > 0:
                    self.integral_mat[i][j] += self.integral_mat[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.integral_mat[row2][col2]
        if row1 > 0:
            res -= self.integral_mat[row1 - 1][col2]
        if col1 > 0:
            res -= self.integral_mat[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            res += self.integral_mat[row1 - 1][col1 - 1]
        return res
