class Solution_1:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)


# below much faster
from functools import lru_cache
class Solution_2:
    @lru_cache(maxsize=None)  # lru_cache() is a decorator that helps in reducing function execution for the same inputs using the memoization technique
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n-1) + self.fib(n-2)
