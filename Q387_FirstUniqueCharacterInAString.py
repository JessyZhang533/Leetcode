class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1

        for j in dic:  # no index in dictionaries, but would still iterate from the first key appended
            if dic[j] == 1:
                return s.index(j)
        return -1

    def firstUniqChar_2(self, s: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = []
        for i in letters:
            if s.count(i) == 1:
                index.append(s.index(i))
        return min(index) if len(index) > 0 else -1