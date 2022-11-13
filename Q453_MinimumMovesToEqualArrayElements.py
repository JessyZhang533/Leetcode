class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        min_num = nums[0]
        return sum(nums) - min_num * len(nums)

# Essentialy a math question.
# Say, after m moves, we manage to get all elements as x, then:
# sum + m * (n - 1) = x * n
# !!! Also, we need to increment the smallest number at every step
# so: min_num + m = x
# so: m = sum - minNum * n
