class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        "https://leetcode.com/problems/maximal-square/solutions/600149/python-thinking-process-diagrams-dp-approach/"
        r, c = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(c+1)] for _ in range(r+1)]
        max_side = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':  # note that matrix[i][j] and dp[i+1][j+1] refer to the same position
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i][j], dp[i+1][j]) + 1
                    max_side = max(max_side, dp[i+1][j+1])
        return max_side * max_side
