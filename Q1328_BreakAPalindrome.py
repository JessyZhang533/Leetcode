class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(len(palindrome) // 2):  # check half of the palindrome
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]  # turn the first non-a letter to a
        return palindrome[:-1] + 'b' if palindrome[:-1] else ''  # two edge cases: 1.letters are all a; 2.only one letter is in the palindrome
