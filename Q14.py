# Longest common prefix

# test of method 2
str = ["annnnn", "b", "kie", "annn", "Annnn"]
print(min(str))
print(max(str))

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
    # 1. Strings starting with uppercase will be proiritised
    # 2. Sort the first letter by alphebetical order
    # 3. Sort by length of string
    def longestCommonPrefix_2(self, m):
        if not m: return ''
		# since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(m)
        s2 = max(m)

        for i, c in enumerate(s1):  # !!! this function saves the trouble of considering iterating over indices or items
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1
