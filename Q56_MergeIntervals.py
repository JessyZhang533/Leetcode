# Merge Intervals

class Solution:
    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i[0]): # sort by starting time of intervals
            if out and i[0] <= out[-1][1]:  # !!! out[-1]
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out += [i]  # essentially out.append(i)
        return out
