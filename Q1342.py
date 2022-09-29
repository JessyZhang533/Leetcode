# Number of steps to reduce a number to zero

class Solution:
    def numberOfSteps_1(self, num: int) -> int:
        i = 0
        while num:
            if not num%2:
                num = num/2
                i += 1
            else:
                num = num - 1
                i += 1
        return i

    def numberOfSteps_2(self, n: int) -> int:
        c = 0
        while n != 0: n, c = n - 1 if n % 2 else n//2, c + 1  # 'n, c' means declaring variables. It doesn't mean 'c = n-1'
        return c
