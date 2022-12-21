class Solution:
    def titleToNumber_1(self, columnTitle: str) -> int:
        res, n = 0, 0
        while n < len(columnTitle):
            res = res + (ord(columnTitle[n]) - ord('A') + 1) * 26**(len(columnTitle)-n-1)
            n += 1
        return res

    def titleToNumber_2(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter)-64
            ans += digit * 26**pos
            pos += 1
        return ans
