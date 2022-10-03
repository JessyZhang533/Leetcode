# String to integer

class Solution:
    # 1. .strip(): trim white space
    # 2. .isdigit(): check if the instance in text id a digit
    # 3. when faces with 32-bit limit checks, better check while adding digits up; use .ord(): returns an integer representing the Unicode character.
    def myAtoi(self, s: str) -> int:
        
        MAX_NUM = 2 ** 31 - 1
        MIN_NUM = -2 ** 31
        
        # trim the leading white space first
        s = s.strip()
        sign = 1
        index = 0
        num = 0
        if not s:
            return num
        
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
        
        while index < len(s) and s[index].isdigit():
            curr_digit = ord(s[index]) - ord('0')
            if num > MAX_NUM // 10 or (num == MAX_NUM // 10 and curr_digit > 7): # here we do the check before adding current digit
                return MAX_NUM if sign == 1 else MIN_NUM  # if statement
            num = num * 10 + curr_digit  # !!!
            index += 1
        
        num = sign * num
        return num