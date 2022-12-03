class Solution:
    # 1.any(): returns True if any element of an iterable is True. If not, it returns False
    # 2.The '+=' and ',' in line 7: The comma actually changes the assignment value to be a tuple (iterable) and therefore extends the array
    def wordBreak_1(self, s: str, wordDict: List[str]) -> bool:
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),  # if 'ok[j] and s[j:i] in wordDict' is True, then we can successfuly split out a word in s that belongs to wordDict
        return ok[-1]

    # The following is an explanation of method 1
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ok = [True]
        for i in range(1, len(s)+1):
            list_i = []
            for j in range(i):
                list_i.append(ok[j] and s[j:i] in wordDict)
            if True in list_i:
                ok.append(True)
            else:
                ok.append(False)
            print(ok)
        return ok[-1]
