class Solution:
    def strStr_1(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        i = 0
        while i < len(haystack):
            k = i
            for j in needle:
                if j != haystack[k]:
                    break
                k += 1
            if k == i + len(needle):
                return i
            i += 1

    def strStr_2(self, haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
