class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])
        
        # !!!: 4 pointers
        top = 0
        bottom = height - 1
        left = 0
        right = width - 1
        
        ans = []
        # Better to use for and while loops instead of if statements
        while top < bottom and left < right:  # These twoconditions will not be met at the same time if matrix is not square
            for col in range(left, right):  # Doesn't include 'right'
                ans.append(matrix[top][col])
            for row in range(top, bottom):  # Doesn't include 'bottom'
                ans.append(matrix[row][right])
            for col in range(right, left, -1):  # Doesn't include 'left'
                ans.append(matrix[bottom][col])
            for row in range(bottom, top, -1):  # Doesn't include 'top'
                ans.append(matrix[row][left])
            # Move pointers
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        # If a matrix remain inside it is either a 1xn or a mx1
        # a linear scan will return the same order as spiral for these
        if len(ans) < height*width:
            for row in range(top, bottom+1):  # !!!: note the +1
                for col in range(left, right+1):  # !!!: note the +1
                    ans.append(matrix[row][col])
        
        return ans
