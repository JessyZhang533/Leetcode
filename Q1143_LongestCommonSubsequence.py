class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        " similar to Q516 "
        text1, text2 = '!'+text1, '!'+text2
        m, n = len(text1), len(text2)
        dp = [[0]*n for _ in range(m)]  # dp[i][j] denotes the length of longest common sequence of text1[:i] and text2[:j]
        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
