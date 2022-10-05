# Pairs of Songs With Total Durations Divisible by 60

# (x + i) % 60 = 0 --> x % 60 = 60 - t % 60
# exception: x%60 = i%60 = 0
class Solution:
    def numPairsDivisibleBy60(self, time):
        c = [0] * 60  # i in c represent the number of items in 'time' that satisfies i%60 = time.index(i)
        res = 0
        for t in time:  # find pairs and append at the same time
            res += c[-t % 60]
            c[t % 60] += 1
        return res
