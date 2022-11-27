class Solution:
    def plusOne_1(self, digits: List[int]) -> List[int]:
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

    # The pow(x, y) function returns the value of x to the power of y (x^y).
    def plusOne_2(self, digits: List[int]) -> List[int]:
        " Convert to number, then to string, then to list "
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]
