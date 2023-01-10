# Decode ways
# DYNAMIC PROGRAMMIN

class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case check
        if s is None or s[0] == '0':
            return 0

        # dp[i] is the number of ways to parse s[:i]
        dp = [1] * len(s)  # elements set to 1 instead of 0, because we need to initiliase the first entry to 1
        # (at this stage it must be a non-zero integer and thus can be decoded)
        for i in range(1, len(s)):
            # One digit check
            dp[i] = 0 if int(s[i]) == 0 else dp[i - 1]
            # Two digit check
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i - 2 if i > 1 else 0]  # equivalent to: else dp[i]+=1
        # Return the last element
        return dp[-1]

    # explanation of the above method
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp = [1]*len(s)
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i] = dp[i-1]
            else:
                dp[i] = 0
            
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2 if i>1 else 0]
        return dp[-1]
