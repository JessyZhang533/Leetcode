class Solution:
    # both methods: dp, dp[i] is the max product for target i
    def integerBreak_1(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(3, len(dp)):
            dp[i] = max(max(dp[i-m]*m, (i-m)*m) for m in range(1, i))  # !!! include (i-m)*m
        return dp[-1]
        
    def integerBreak_2(self, n: int) -> int:
        " Spot the math pattern, realize that we should split numbers into 2 and 3, then use dp "
        # https://leetcode.com/problems/integer-break/solutions/285876/python-o-1-one-line-solution-detailed-explanation/
        case = [0,0,1,2,4,6,9]
        if n < 7:
            return case[n]
        dp = case + [0] * (n-6)
        for i in range(7, n+1):
            dp[i] = 3*dp[i-3]
        return dp[-1]
