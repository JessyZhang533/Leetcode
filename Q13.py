# Roman to integer

class Solution:
    def romanToInt_1(self, s: str) -> int:
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1:
                if s[i] == "I" and s[i+1] == "V":
                    result += 4
                    i += 2
                elif s[i] == "I" and s[i+1] == "X":
                    result += 9
                    i += 2
                elif s[i] == "X" and s[i+1] == "L":
                    result += 40
                    i += 2
                elif s[i] == "X" and s[i+1] == "C":
                    result += 90
                    i += 2
                elif s[i] == "C" and s[i+1] == "D":
                    result += 400
                    i += 2
                elif s[i] == "C" and s[i+1] == "M":
                    result += 900
                    i += 2
                else:
                    result += dic[s[i]]
                    i += 1
            else:
                result += dic[s[i]]
                i += 1
        return result

    # 1.Romans using subtraction such as IV, IX are annoying. So we just replace them with 'normal' logic, i.e.IIII, VIIII
    # 2.str.replace(): The replace() method returns a copy of the string where the old substring is replaced with the new substring. The original string is unchanged.
    # If the old substring is not found, it returns the copy of the original string.
    def romanToInt_2(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        # These 3 lines can be written as: s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        # (run time decreases, memory increases)
        for char in s:
            number += translations[char]
        return number
