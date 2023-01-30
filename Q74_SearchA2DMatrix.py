class Solution:
    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        m, n = len(matrix), len(matrix[0])
        row_num = 0
        while row_num < m:
            if target < matrix[row_num][0]:
                return False
            elif target > matrix[row_num][-1]:
                row_num += 1
            else:
                break
        if target in matrix[row_num]:
            return True
        else:
            return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        " Binary search; O(logmn) "
        m, n = len(matrix), len(matrix[0])
        l, h = 0, m*n  # not m*n-1, because if the matrix has one single entry, then l=h=0, and the while loop will be completely skipped
        while l < h:
            mid = (l + h) // 2
            num = matrix[mid // n][mid % n]
            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                h = mid  # reason same as 'm*n'
        return False
        