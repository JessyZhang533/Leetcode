class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)  # !!!: search in set is O(1)
        longest = 0
        for x in nums:
            if x-1 not in nums:
                y = x + 1  # !!!: y itself can keep track of the length
                while y in nums:
                    y += 1
                longest = max(longest, y - x)
        return longest
