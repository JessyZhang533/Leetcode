from functools import lru_cache


class Solution_1:
    @lru_cache
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)


class Solution_2:
    # Dynamic programming
    def tribonacci(self, n):
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp[i % 3] = sum(dp)  # !!!
        return dp[n % 3]