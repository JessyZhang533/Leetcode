class Solution:
    # dynammic programming
    # top-down
    def rob_1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        money = [0]*len(nums)
        money[0], money[1] = nums[0], nums[1]
        for i in range(2, len(nums)):
            if i-3 >= 0:
                money[i] = max(money[i-2] + nums[i], money[i-3] + nums[i])  # !!! similar to climbing stairs
            else:
                money[i] = money[i-2] + nums[i]
        return max(money[-1], money[-2])

    def rob_2(self, A):  # t.c. O(N), s.c. O(1)
        prev2, prev, cur = 0, 0, 0  # 3 variables tracking the sum
        for i in A:
            cur = max(prev, i + prev2)
            prev2 = prev
            prev = cur
        return cur
