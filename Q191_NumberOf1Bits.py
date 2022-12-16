class Solution:
    # bin(): converts a specified integer number to its binary representation and returns it; the prefix '0b' in the output represents that the result is a binary string
    def hammingWeight_1(self, n: int) -> int:
        count = 0
        for i in range(2, len(str(bin(n)))):
            if str(bin(n))[i] == '1':
                count += 1
        return count

    def hammingWeight_2(self, n: int) -> int:
        return bin(n).count('1')

    def hammingWeight_3(self, n: int) -> int:
        " If we have number n, then n&(n-1) will remove the rightmost in binary representation of n. For example if n = 10110100, then n & (n-1) = 10110100 & 10110011 = 10110000 "
        count = 0
        while n:
            n &= n-1
            count += 1
        return count
