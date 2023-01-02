from functools import lru_cache
class Solution:
    @lru_cache
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
