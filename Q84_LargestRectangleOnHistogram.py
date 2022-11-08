class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        " for given bar i with value h, how to find the biggest rectangle, which is ending with this bar?  "
        # stack store indices; values corresponding to these indices are in ascending order
        stack, ans = [], 0
        for i, h in enumerate(heights + [0]):  # !!!: + [0]
            while stack and heights[stack[-1]] >= h:
                H = heights[stack.pop()]
                W = i if not stack else i-stack[-1]-1
                ans = max(ans, H*W)
            stack.append(i)
        return ans
