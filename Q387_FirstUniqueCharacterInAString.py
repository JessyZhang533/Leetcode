class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1

        for j in dic:
            if dic[j] == 1:
                return s.index(j)
        return -1