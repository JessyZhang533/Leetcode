class Solution:
    def isPowerOfThree_1(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 3:
            return False
        i = 3
        while i <= n:
            if i == n:
                return True
            i *= 3
        return False

    def isPowerOfThree_2(self, n: int) -> bool:
        " O(1); 3^19(1,162,261,467) is the largest power of three under 2^31 - 1 "
        return (n > 0) and 1162261467 % n == 0
