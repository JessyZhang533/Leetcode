class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0]*n  # dp[i] is the ith ugly number
        dp[0] = 1
        p1, p2, p3 = 0, 0, 0  # 3 pointers, pointing at the smallest number need to multiply by 2, 3, 5
        for i in range(1, n):
            dp[i] = min(dp[p1]*2, dp[p2]*3, dp[p3]*5)  # This method made sure that dp[i], i>=1 only consist of factors 2, 3, 5
            # use 3 parallel if statements instead of if, elif, else
            # beacause we need to ensure that for numbers that are the common multiple of 2, 3, 5, we will move all related pointers at the same time
            if dp[i] == dp[p1]*2:
                p1 += 1
            if dp[i] == dp[p2]*3:
                p2 += 1
            if dp[i] == dp[p3]*5:
                p3 += 1
        return dp[-1]
