class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        " 1-d dp; please note this dp is only valid for all entries NON-NEGATIVE "
        m, n = len(grid), len(grid[0])
        dp = [0] + [float('inf')]*(n-1)  # dp list, length=number of columns, dp[k] is the minimum sum at column k, row unknown (determined by the outer for loop)
        for i in range(m):
            dp[0] += grid[i][0]  # dp[0] is the sum going straight down from [0][0] to [i][0]
            for j in range(1, n):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]  # if dp[j-1] is smaller, go right; if dp[j] is smaller, equivalent to going down
        return dp[-1]
