class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans , prefsum, d = 0,  0, {0:1}
        # presum is the prefix sum from index 0 to current index
        # d is a dictionary; key is the prefix sum, value is the number of subsequences with the corresponding prefix sum
        # d initialised to {0:1} because we need d[prefsum-k] = 1 when prefsum=k
        for num in nums:
            prefsum += num
            ans = ans + d.get(prefsum-k, 0)  # complementary method: no. of sequences sum up to (prefsum-k) = no. of sequences sum up to (k)
            d[prefsum] = d.get(prefsum, 0) + 1
        return ans
        # d.get(key, val): return d[key] if key in d, else retu0n 0
