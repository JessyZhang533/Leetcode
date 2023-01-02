# Basically Fibonacci (Q509, Q1137)
from functools import lru_cache


class Solution:
    def climbStairs_1(self, n):
        " Bottom Up "
        if n == 1:
            return 1
        res = [0 for _ in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]  # !!!
        return res[-1]

    def climbStairs_2(self, n):
        " Top Down "
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)

    def climbStairs_3(self, n):
        " a is the number of ways to reach the current step, b is the number of ways to reach the next step "
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def climbStairs_4(self, n):
        " Dynamic programming; see Q1137 "
        dp = [1, 2]
        for i in range(2, n):  # note start and end!
            dp[i % 2] = sum(dp)  # i or i-1 or i+1?
            print(dp)
        return dp[(n+1) % 2]  # n+1 not n

    @lru_cache
    def climbStairs_5(self, n):
        if n < 3:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        