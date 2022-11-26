class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def handle(digits, i):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            else:
                digits[i] = 0
                if i > 0:
                    return handle(digits, i-1)
                else:
                    digits.insert(0, 1)
                    return digits
        return handle(digits, len(digits)-1)
