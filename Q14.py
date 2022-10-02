# Longest common prefix

class Solution:
    def longestCommonPrefix_1(self, strs: List[str]) -> str:
        min_len_word = min(strs)
        prefix = ""
        for i in range(len(min_len_word)):
            for j in strs:
                if j[i] != min_len_word[i]:
                    return prefix
            prefix += min_len_word[i]
        return prefix

    # min() and max() used on a list of strings
    def longestCommonPrefix_2(self, m):
        if not m: return ''
		# since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(m)
        s2 = max(m)

        for i, c in enumerate(s1):  # !!! this function saves the trouble of considering iterating over indices or items
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1
