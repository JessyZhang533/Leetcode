class Solution_1:
    # two pointers
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):  # For every letter, run odd/even case helper to find palindromic string
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)  # Should specify the key
        return res
 
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer: string with odd length, then originally l=r; string with ecen length, then originally r=l+1
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]


class Solution_2:
    # dp
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        # dp[i][j] represents whether s[i][j] is a palindromic string
        # i<=j, so dp is an upper triangular matrix
        res_start, res_end = 0, 0

        # s[i][i] is always a palindrome, so diagonal cells of dp are all True
        for i in range(n):
            dp[i][i] = True

        # update dp
        for end in range(n):
            for start in range(end-1, -1, -1):
                if s[start] == s[end]:
                    if end-start==1 or dp[start+1][end-1]:  # !!!
                        dp[start][end] = True
                        if end-start+1 > res_end-res_start+1:  # update result
                            res_start = start
                            res_end = end
        return s[res_start:res_end+1]
