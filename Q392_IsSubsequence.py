class Solution:
    def isSubsequence_1(self, s: str, t: str) -> bool:
        if not s:
            return True  # !!!
        elif not t:
            return False

        i = 0
        for char in t:
            if i < len(s):  # !!!: check index first
                if char == s[i]:
                    i += 1
            else:
                break
        return i == len(s)

    def isSubsequence_2(self, s: str, t: str) -> bool:
        " dp https://leetcode.com/problems/is-subsequence/solutions/678389/python-3-solutions-dp-2-pointers-follow-up-bs-explained/"
        s, t = '!'+s, '!'+t
        m, n = len(s), len(t)
        dp = [[0]*m for _ in range(n)]  # Let dp[i][j] = 1 if s[:j] is substring of t[:i]; upper triangular part of dp will all be 0
        for k in range(n):
            dp[k][0] = 1  # when s is empty, s will always be a valis subsequence
        for i in range(1, n):
            for j in range(1, m):  # the upper limit is 'm' not 'i', because usually m is less than n; if m>i, dp[i][j] will just be 0
                if s[j] == t[i]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
