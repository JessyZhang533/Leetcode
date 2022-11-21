class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # top-down approach: start from the end of list, see if can reach the beginning of list
        last_pos = len(nums) - 1  # last_pos is the essentially the smallest index that can reach the end of list
        for i in range(len(nums)-2, -1, -1):
            if (i + nums[i]) >= last_pos:
                last_pos = i
        return last_pos == 0
