class Solution:
    def removeElement_1(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                j = i
                while nums[j] == val:
                    if j == len(nums) - 1:
                        return i
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]

    def removeElement_2(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[k] = nums[i]  # k points at the first element == val; set value only, no need to swap
            k += 1
        return k
