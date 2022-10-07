# Meeting rooms 2

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq  # min heap
        heap = []  # A list of end times
        for i in sorted(intervals, key=lambda x:x[0]):
            if heap and heap[0] <= i[0]:  # If the new start time is greater than or equal to the existing earliet end time
                heapq.heapreplace(heap, i[-1])  # pop old existing earliest ending time, push new ending time to the list
            else:
                heapq.heappush(heap, i[-1])  # The room is still in use, add (push a new end time to min heap) a new room
        return len(heap)
