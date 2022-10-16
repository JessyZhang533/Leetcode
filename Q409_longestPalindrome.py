class Solution:
    def longestPalindrome_1(self, s: str) -> int:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        odd_num = 0
        for j in dic:
            if dic[j] % 2:
                odd_num += 1

        if odd_num == 0:
            return len(s)
        else:
            return len(s) - odd_num + 1  # !!!

    def longestPalindrome_2(self, s): # much quicker
        """
        :type s: str
        :rtype: int
        """
        hash = set()  # !!! set has no duplicates
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)