class Solution:
    def secondHighest_1(self, s: str) -> int:
        dic = {}
        for i in s:
            if i.isdigit():
                if i not in dic.keys():
                    dic[i] = int(i)
        list_of_digits = list(dic.keys())
        if len(list_of_digits) < 2:
            return -1
        else:
            list_of_digits.sort()
            return list_of_digits[-2]

    def secondHighest_2(self, s: str) -> int:
        first = sec = -1  # two pointers
        for c in s:
            if c.isdigit():
                d = ord(c) - ord('0')  # !!! use ascii to convert digit to string
                if first < d:
                    sec, first = first, d
                elif sec < d and d < first:
                    sec = d
        return sec
