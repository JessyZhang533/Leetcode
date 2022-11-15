class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}  # key: words; value: length of word chain
        for w in sorted(words, key=len):  # firstly, dort the word list by length
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))  # dictionary.get()
        return max(dp.values())
