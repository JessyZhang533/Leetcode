class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)  # .add(): adds a given element to a set. If the element is already present, it doesn't add any element.
            n = sum([int(x) ** 2 for x in str(n)])  # conversion between string and integer; sum()
        # Note: if n turns 1 in the loop, then n will always be 1^2=1 and will not change anymore
        return n == 1
