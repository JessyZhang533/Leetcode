# Basically Fibonacci

class Solution:
    def climbStairs_1(self, n):
        " Bottom Up "
        if n == 1:
            return 1
        res = [0 for _ in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]  # !!!
        return res[-1]

    def climbStairs_2(self, n):
        " Top Down "
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)

    def climbStairs_3(self, n):
        " a is the number of ways to reach the current step, b is the number of ways to reach the next step "
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a
