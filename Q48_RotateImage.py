class Solution:
    def rotate_1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        " Transpose + symmetry of vertical axis "
        n = len(matrix)
        # !!! TAKING TRANSPOSE
        for m in range(n):
            for k in range(m):  # !!! is range(m) instead of range(n)
                matrix[m][k], matrix[k][m] = matrix[k][m], matrix[m][k]

        for i in range(n//2):
            for j in range(n):
                matrix[j][i], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[j][i]

    def rotate_2(self, matrix: List[List[int]]) -> None:
        " Reverse rows + transpose "
        # reverse
        l = 0
        r = len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        # transpose 
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
