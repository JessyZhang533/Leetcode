class Solution:
    # Similar to 3Sum, but too slow
    def threeSumClosest_1(self, num, target):
            num.sort()
            result = num[0] + num[1] + num[2]
            for i in range(len(num) - 2):
                if i > 0 and num[i] == num[i-1]:  # here we skip if the number on index i appears before
                    continue
                j, k = i+1, len(num) - 1
                while j < k:
                    sum = num[i] + num[j] + num[k]
                    if sum == target:
                        return sum
                    if abs(sum - target) < abs(result - target):
                        result = sum
                    if sum < target:  # just move pointers, don't over somplicate
                        j += 1
                    else:  # just move pointers, don't over somplicate
                        k -= 1            
            return result

    # Use 3 pointers as well
    def threeSumClosest_2(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = 2147483647  # assign the largest number
        
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(closest - target):
                    closest = s
                    
                if s < target:
                    l += 1
                    while l < r and nums[l] == nums[l+1]:  # here we skip if the number on index i appears before
                        l += 1
                elif s > target:
                    r -= 1
                    while l < r and nums[r] == nums[r-1]:  # here we skip if the number on index i appears before
                        r -= 1
                else:
                    return s
        
        return closest