class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(16):
            right_bit = (n>>i)&1
            left_bit = (n>>(31-i))&1
            ret |= right_bit<<(31-i)
            ret |= left_bit<<i
        return ret  
