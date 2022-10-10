class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            # The following line do all the work in terms of selectig the maximum water area
            max_water = max(max_water, min(height[left], height[right]) * (right - left))
            # If statement: discard the smaller one of height[left] and height[right]
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
