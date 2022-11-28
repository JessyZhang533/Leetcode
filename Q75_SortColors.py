class Solution:
    def sortColors_1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        " Insertion sort: a great way to sort lists in-place "
        for i in range(1, len(nums)):
            temp = nums[i]
            for j in range(i-1,-1,-1):
                if temp < nums[j]:
                    nums[j+1] = nums[j]
                    nums[j] = temp

    def sortColors_2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)-1
        
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
                # do not movepointer white because nums[blue] is unchecked
