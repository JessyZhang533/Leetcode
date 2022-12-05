class Solution:
    def numSquares(self, n: int) -> int:
        " BFS "
        if n < 2:  # handle edge case
            return n

        lst = []  # a list with perfect squares (less than n)
        i = 1
        while i * i <= n:  # construct lst
            lst.append(i * i)
            i += 1

        cnt = 0
        toCheck = {n}  # this is a set with one element
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:  # y is a perfect square number 
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y) # In the 1st iteration, temp has elements (n-lst[0]), (n-lst[1]), (n-lst[2])...
            toCheck = temp  # set toCheck becomes set temp

        return cnt
