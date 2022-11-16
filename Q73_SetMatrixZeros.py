class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # two booleans to check if 1st row and col needs to be filled with 0
        first_r_has_zero = False
        first_c_has_zero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_r_has_zero = True
                    if j == 0:
                        first_c_has_zero = True
                    matrix[i][0], matrix[0][j] = 0, 0
        for p in range(1, m):
            for q in range(1, n):
                if matrix[0][q] == 0 or matrix[p][0] == 0:
                    matrix[p][q] = 0
        # we used the 1st row & column as trackers, but we didn't fill them with 0 if they needed to
        if first_r_has_zero:
            for h in range(n):
                matrix[0][h] = 0
        if first_c_has_zero:
            for g in range(m):
                matrix[g][0] = 0

# The approach to get constant space is to use first row and first col of the matrix as a tracker.

# At each row or col, if you see a zero, then mark the first row or first col as zero with the current row and col.
# Then iterate through the array again to see where the first row and col were marked as zero and then set that row/col as 0.
# After doing that, you'll need to traverse through the first row and/or first col if there were any zeroes there to begin with and set everything to be equal to 0 in the first row and/or first col.
