class Solution:
    def intToRoman_1(self, num: int) -> str:
        list_of_dic = [["I", "V"], ["X", "L"], ["C", "D"], ["M"]]
        res = ""
        digit = 0
        divisor_co = 3
        while num:
            digit = num // 10**divisor_co
            num = num % (10**divisor_co)
            if digit == 0:
                divisor_co -= 1
                continue
            elif digit < 4:
                res = res + list_of_dic[divisor_co][0]*digit  # !!!: we cannot use '.append' to a string, use addition instead
            elif digit == 4:
                res = res + list_of_dic[divisor_co][0] + list_of_dic[divisor_co][1]
            elif digit < 9:
                res = res + list_of_dic[divisor_co][1] + list_of_dic[divisor_co][0]*(digit - 5)
            else:
                res = res + (list_of_dic[divisor_co][0] + list_of_dic[divisor_co + 1][0])
            divisor_co -= 1
        return res

    def intToRoman_2(self, num: int) -> str:
        # Create a dic with 4 related and 9 related numbers included
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ""
        for i in d:
            res += (num//i) * d[i]
            num %= i
        return res
