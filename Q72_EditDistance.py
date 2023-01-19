# https://leetcode.com/problems/edit-distance/solutions/25846/c-o-n-space-dp/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        t1, t2 = '!'+word1, '!'+word2
        m, n = len(t1), len(t2)
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j
        for i in range(1, m):
            for j in range(1, n):
                if t1[i] == t2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])  # 3 cases: delete, insert, replace
        return dp[-1][-1]
