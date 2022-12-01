class Solution:
    def largestNumber_1(self, nums: List[int]) -> str:
        " selection Sort "
        def compare(n1, n2): # !!!
            return str(n1) + str(n2) > str(n2) + str(n1) # !!! just like comparing integers

        for i in range(len(nums), 0, -1):
            tmp = 0
            for j in range(i):
                if not compare(nums[j], nums[tmp]):
                    tmp = j
            nums[tmp], nums[i-1] = nums[i-1], nums[tmp] # nums[tmp] should be put at the rightmost
        return str(int("".join(map(str, nums))))

    def largestNumber_2(self, nums: List[int]) -> str:
        " Bubble sort "
        def compare(n1, n2):
            return str(n1) + str(n2) > str(n2) + str(n1)

        for i in range(len(nums), 0, -1):
            for j in range(i-1):
                if not compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return str(int("".join(map(str, nums))))

class Solution:
    def largestNumber3(self, nums: List[int]) -> str:
        " merge sort "
        nums = self.mergeSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

    def mergeSort(self, nums, l, r):
        if l > r:
            return
        if l == r:
            return [nums[l]]
        mid = l + (r-l)//2
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid+1, r)
        return self.merge(left, right)

    def merge(self, l1, l2):
        res, i, j = [], 0, 0
        while i < len(l1) and j < len(l2):
            if not self.compare(l1[i], l2[j]):
                res.append(l2[j])
                j += 1
            else:
                res.append(l1[i])
                i += 1
        res.extend(l1[i:] or l2[j:])
        return res

class Solution:
    " quick sort "
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

    def largestNumber_4(self, nums):
        self.quickSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums)))) 

    def quickSort(self, nums, l, r):
        if l >= r:
            return 
        pos = self.partition(nums, l, r)
        self.quickSort(nums, l, pos-1)
        self.quickSort(nums, pos+1, r)
        
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low