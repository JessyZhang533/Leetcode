# Trapping rain water

# https://leetcode.com/problems/trapping-rain-water/solutions/1374608/c-java-python-maxleft-maxright-so-far-with-picture-o-1-space-clean-concise/?orderBy=most_votes

class Solution:
    def trap_1(self, height: List[int]) -> int:
        " Max left & max right as lists "
        n = len(height)
        maxleft, maxright = [0]*n, [0]*n
        for i in range(1, n):
            maxleft[i] = max(maxleft[i-1], height[i-1])
        for j in range(n-2, -1, -1):
            maxright[j] = max(maxright[j+1], height[j+1])

        ans = 0
        for i in range(n):
            waterlevel = min(maxleft[i], maxright[i])
            if waterlevel > height[i]:
                ans += waterlevel - height[i]

        return ans

    def trap_2(self, height: List[int]) -> int:
        " Max left & max right as pointers "
        if len(height) <= 2: return 0
        n = len(height)
        maxLeft, maxRight = height[0], height[n-1]
        left, right = 1, n - 2
        ans = 0
        while left <= right:
            if maxLeft < maxRight:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    ans += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    ans += maxRight - height[right]
                right -= 1
        return ans

        