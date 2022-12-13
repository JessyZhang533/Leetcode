from functools import reduce


class Solution:
    def singleNumber_1(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num  # ^: https://stackoverflow.com/questions/2451386/what-does-the-caret-operator-do
            # !!! 1 xor 2 xor 3 xor 1 xor 2 xor 3 xor 4 = (1 xor 1) xor (2 xor 2) xor (3 xor 3) xor 4 (commutative & associative)
        return xor

    def singleNumber_2(self, nums: List[int]) -> int:
        return reduce(lambda total, el: total ^ el, nums)  # reduce(fuction, sequence): https://thepythonguru.com/python-builtin-functions/reduce/
        