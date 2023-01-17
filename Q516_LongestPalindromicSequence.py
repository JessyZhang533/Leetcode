class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        " dp similar to Q5 "
        n = len(s)
        dp = [[0]*n for _ in range(n)]  # dp[i][j] denotes the length of the longest palindromic subsequence of s[l..r] (indices inclusive)
        for start in range(n-1, -1, -1):
            dp[start][start] = 1  # s[i][i] is a length 1 palindrome
            for end in range(start+1, n):
                if s[start]==s[end]:
                    dp[start][end] = dp[start+1][end-1] + 2
                else:
                    dp[start][end] = max(dp[start+1][end], dp[start][end-1])
        return dp[0][n-1]  # from index 0 to index n-1 inclusive
