class Solution:
    def pivotIndex_1(self, nums: List[int]) -> int:
        if len(nums) == 1:  # !!!
            return 0
        l_1 = [0]*len(nums)
        l_2 = [0]*len(nums)

        for i in range(len(nums)):
            if i > 0:
                l_1[i] = l_1[i - 1] + nums[i]
            else:
                l_1[i] = nums[i]
        for j in range(len(nums)-1, -1, -1):
            if j < len(nums) - 1:
                l_2[j] = l_2[j + 1] + nums[j]
            else:
                l_2[j] = nums[j]
        print(l_1, l_2)
        for k in range(len(nums)):
            if k == 0:
                if l_2[1] == 0:
                    return 0
            elif k == len(nums)-1:
                if l_1[len(nums)-2] == 0:
                    return len(nums)-1
            else:
                if l_1[k-1] == l_2[k+1]:
                    return k
        return -1

    def pivotIndex_2(self, nums):
        # Time: O(n)
        # Space: O(1)
        left, right = 0, sum(nums)  # use of sum()
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1
        
        