class Solution:
    # bitwise operators https://realpython.com/python-bitwise-operators/
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(16):
            right_bit = (n>>i)&1  # equals 1 if last bit of n>>i is 1; equals 0 if last bit of n>>i is 0
            left_bit = (n>>(31-i))&1
            ret |= right_bit<<(31-i)
            ret |= left_bit<<i
        return ret 
