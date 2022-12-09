class Solution:
    def reverseString_1(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def reverseString_2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]  # !!! not 's=s[::-1]'. 's[:] =' is editing the actual memory bytes s points to, and 's =' points the variable name s to other bytes in the memory.
