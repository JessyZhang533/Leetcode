class Solution:
    def wiggleMaxLength_1(self, nums: List[int]) -> int:
        " Maximise the number of peaks and valleys "
        up, down = 1, 1
        # up is the number of peaks & valeys when the last element is peak
        # down is the number of peaks & valleys when the last element is valley
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                down = up + 1
            elif nums[i-1] < nums[i]:
                up = down + 1
            #  eg. if nums[i-2]<nums[i-1]<nums[i], then we will run 'up=down+1' twice.
            # Note that 'down' won't change in these two operations,
            # so value of 'up' after the first operation will be the same as that after the second operation
        return max(up, down)

    def wiggleMaxLength_2(self, nums: List[int]) -> int:
        length = 1
        up = None
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i] and up != False:
                length += 1
                up = False
            if nums[i-1] < nums[i] and up != True:
                length += 1
                up = True
        return length
