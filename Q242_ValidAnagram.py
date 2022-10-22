class Solution:
    def isAnagram_1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic_s = {}
        for m in s:
            if m not in dic_s:
                dic_s[m] = 1
            else:
                dic_s[m] += 1
        for i in t:
            if i in dic_s:
                dic_s[i] -= 1
            else:
                return False
        for j in dic_s.values():
            if j != 0:
                return False
        return True

    def isAnagram_2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram_3(self, s, t):
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2  # !!!: if keys and values are the same, the dics are the same. (we do not index into dics)

    # The ord() function in Python is used to convert a single Unicode character to its integer equivalent.
    # (integer representation of letters are consecutive)
    def isAnagram_4(self, s, t):
        dic1, dic2 = [0]*26, [0]*26
        for item in s:
            dic1[ord(item)-ord('a')] += 1
        for item in t:
            dic2[ord(item)-ord('a')] += 1
        return dic1 == dic2
