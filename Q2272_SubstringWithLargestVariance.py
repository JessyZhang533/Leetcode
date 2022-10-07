# Substring with Largest Variance

from itertools import permutations  # permutations: Return successive r length permutations of elements in the iterable.
from collections import Counter  # Counter: a collection where elements are stored as dictionary keys and their counts are stored as dictionary values
# https://leetcode.com/problems/substring-with-largest-variance/solutions/2041108/python3-enumerate-all-a-b-combinations-and-do-maximum-subarray/


class Solution:
    def largestVariance(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        for a, b in permutations(counter, 2):  # Use permutations instead of combinations, cuz a substring with 3a, 1b != a substring with 3b, 1a
            max_subarray = 0
            has_a, has_b = False, False
            remain_a, remain_b = counter[a], counter[b]  # Inicial values: values of occurences of a, b
            for ch in s:
                if ch != a and ch != b:
                    continue
                if max_subarray < 0 and remain_a != 0 and remain_b != 0:  # if now the accumulated substring has more b than a, and westill have a and b lest unchecked
                    max_subarray = 0
                    has_a, has_b = False, False
                if ch == a:
                    max_subarray += 1  # assign +1 to a
                    remain_a -= 1
                    has_a = True
                elif ch == b:
                    max_subarray -= 1  # assign -1 to b
                    remain_b -= 1
                    has_b = True
                if has_a and has_b:
                    res = max(res, max_subarray)  # Note we only want a number, we don't need to return the substring
        return res
