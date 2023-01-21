class Solution:
    def numSquares_1(self, n: int) -> int:
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

    def numSquares_2(self, n: int) -> int:
        " dp[i] is the the least number of perfect square numbers that sum to i "
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            j = 1
            while j*j <= i:  # use a while loop when you can't decide the upper limit
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j+=1  # !!! don't forget
        return dp[-1]
