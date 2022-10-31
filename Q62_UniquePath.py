from functools import cache
from math import factorial


class Solution:
    # M1 & M2: No memory: t.c. O(2^(m+n))
    def uniquePaths_1(self, m: int, n: int) -> int:
        if m < 2 or n < 2:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

    def uniquePaths_2(self, m, n):
        def dfs(i, j):
            if i >= m or j >= n:      return 0
            if i == m-1 and j == n-1: return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)

    # M3: have memory (@cache)
    def uniquePaths_3(self, m, n):
        @cache
        def dfs(i, j):
            if i >= m or j >= n:      return 0
            if i == m-1 and j == n-1: return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)

    # M4: memorize by creating a table
    def uniquePaths_4(self, m, n):
        dp = [[1]*n for i in range(m)]
        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    # M5: math; fastest
    # calculating the number of different ways to choose m-1 down-moves and n-1 right-moves from a total of m+n-2 moves
    def uniquePaths_5(self, m, n):
        return factorial(m+n-2) // factorial(m-1) // factorial(n-1)
