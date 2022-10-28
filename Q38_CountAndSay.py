import itertools


class Solution:
     # groupby(): https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in itertools.groupby(s))
        return s
