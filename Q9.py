# Palindrome number

class Solution:
    def isPalindrome_1(self, x: int) -> bool:
        forward = []
        backward = []
        for i in range(len(str(x))):
            forward.append(list(str(x))[i])
        for j in range(len(str(x)) - 1, -1, -1):
            backward.append(list(str(x))[j])
        if forward == backward:
            return True
        return False

    def isPalindrome_2(self, x: int) -> bool:
        if x < 0:  # negative numbers canot be palindrome
            return False
        newNum = 0
        while x > 0:  # stop when x == 0
            newNum = newNum * 10 + x % 10  # add the digit to the ones place of REVERSED NUMBER
            x = x//10  # truncate the ones place of INPUT NUMBER
        return newNum == x
