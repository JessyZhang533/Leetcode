# The skyline problem
# HARD

import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(L, -H, R) for L, R, H in buildings]  # LIST COMPREHENSION  # adding '-' before height is because teh built-in heap in Python is a min heap
        events += list({(R, 0, 0) for _, R, _ in buildings})  # LIST COMPREHENSION
        events.sort()
        # print(events)

        # res: result, [x, height]
        # live: min heap, [-height, ending position] (live[0] represnts the highest building in the heaap)
        res = [[0, 0]]
        live = [(0, float("inf"))]
        for pos, negH, R in events:
            # print("live is: ", live)
            # print("res is : ", res)

            # 1, pop buildings that are already ended
            while live[0][1] <= pos:
                heapq.heappop(live)  # CURRENT HORIZONTAL LINE ENDS
            # 2, if it's the start-building event, make the building alive
            if negH:
                heapq.heappush(live, (negH, R))  # APPEND BUILDINGS INTO HEAP
            # 3, if previous keypoint height != current highest height, edit the result
            if res[-1][1] != -live[0][0]:
                res += [ [pos, -live[0][0]] ]  # APPEND NEW KEY POINTS INTO RESULT
        return res[1:]


# 1. heapq module: provides implementation of min heap queue algo, ie. priority queue
# heappop(): Pop and return the smallest item from the heap, maintaining the heap invariant
# # https://docs.python.org/3/library/heapq.html
# 2. float("inf"): use an integer to represent it as infinity in Python
