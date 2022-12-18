class Solution:
    def getSum_1(self, a: int, b: int) -> int:
        " bit manipulation "
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits (Python has 64 bits to store inetgers, so we need 'mask' as a new limit between negative and positive)
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits, & gets double 1s, << moves carry
            # binary 0 + 1 = 1
            # binary 1 + 1 = 10
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)

    def getSum_2(self, a: int, b: int) -> int:
        get_sum = [a, b]
        return sum(get_sum)
