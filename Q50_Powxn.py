class Solution:
    def myPow_1(self, x: float, n: int) -> float:
        return x**n

    # https://cp-algorithms.com/algebra/binary-exp.html
    # Binary exponentiation; t.c. O(logn)
    def myPow_2(self, x, n):
        " Recursive "
        if not n:
            return 1
        if n < 0:
            return self.myPow(1 / x, -n)
        if n % 2:
            return x*self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

    def myPow(self, x, n):
        " Iterative "
        if n < 0:
            x = 1 / x
            n = - n
        pow = 1
        while n:
            if n % 2:
                pow *= x
            x *= x
            n //= 2
        return pow