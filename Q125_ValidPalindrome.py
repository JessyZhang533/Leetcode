class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:  # < and <= both will do; becaue if n is odd and we have one last element x unchecked in the middle, we can leave it unchecked of verify x=x
            while l < r and not s[l].isalnum():  # !!! needs condition l < r
                l += 1
            while l < r and not s[r].isalnum():  # !!! needs condition l < r
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True
        