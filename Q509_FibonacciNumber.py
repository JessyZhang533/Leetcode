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


# https://realpython.com/lru-cache-python/

# Wrap:
# What does wrapping mean in programming?
# "Wrap" is a standard English word meaning "Cover or enclose". Typically programmers use it to mean enclosing the functionality of something with something else

# Memorization/Caching:
# This approach ensures that a function doesn’t run for the same inputs more than once by storing its result in memory and then referencing it later when necessary. 

# Least Recently Used (LRU):
# A cache implemented using the LRU strategy organizes its items in order of use. Every time you access an entry, the LRU algorithm will move it to the top of the cache.
# This way, the algorithm can quickly identify the entry that’s gone unused the longest by looking at the bottom of the list.
# The LRU strategy assumes that the more recently an object has been used, the more likely it will be needed in the future, so it tries to keep that object in the cache for the longest time.

# lru_cache:
# Python’s @lru_cache decorator offers a maxsize attribute that defines the maximum number of entries before the cache starts evicting old items.
# By default, maxsize is set to 128. If you set maxsize to None, then the cache will grow indefinitely, and no entries will be ever evicted.
# This could become a problem if you’re storing a large number of different calls in memory.


# Dynamic Programming
class Solution_3:
    def fib(self, n: int) -> int:
        dp = [0,1]
        for i in range(2, n+1):
            dp[i%2] = sum(dp)
        return dp[n%2]
