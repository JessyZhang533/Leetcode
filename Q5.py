# Longest palindromic string

class Solution:
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
