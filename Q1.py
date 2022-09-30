# Two sums

class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):  # DONOT forget 'len'; please check if 'i' represents index or item!!!
            copy = nums.copy()  # list.copy()
            copy.pop(i)  # list.pop(index) returns the item popped; list.remove(item) returns nothing
            if (target - nums[i]) in copy:
                return [i, copy.index(target - nums[i]) + 1]

    # Using dictionary O(n); key-value pair: item-index
    def twoSum_2(self, nums, target):
        d = {}
        for i, n in enumerate(nums):  # The counter of enumerate starts from 0
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i
