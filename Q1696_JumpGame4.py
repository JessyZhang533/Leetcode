class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        " Dynamic programming: modify nums[i] from the original entry to the maximum score we can get to go from index 0 to i "
        n = len(nums)
        dq = deque([0]) 
        # dq store indices of `nums` elements, elements are in decreasing order, the front is the maximum element.
        # dq at most has the length of k+1
        for i in range(1, n):
            # nums[i] = max(nums[i-k], nums[i-k+1],.., nums[i-1]) + nums[i] = nums[dq.front()] + nums[i]
            nums[i] = nums[dq[0]] + nums[i]

            # Add a nums[i] to the deq
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
                # Eliminate elements less or equal to nums[i] from the back (to make sure indices stored in deque indicate elements in decreasing order)
                # Basic reason to pop is that for elements after index i, we would want to jump from the largest value
                # Basic reason to preserve if nums[dq[-1]] > nums[i] is that if the score of i-k to i are all decreasing, when we move to i+1 to calculate its score, we can only make use of i-k+1 (move 'window' to the right by one, and dq in this case has a length of k+1)
            dq.append(i)
            # print(dp)

            # Remove if the last element is out of window size k
            if i - dq[0] >= k:
                dq.popleft()

        return nums[n - 1]

# 1.deque
# deque is implemented as a doubly linked list. So poping and appending from both ends taks O(1). (.pop(), .popleft(), .append(), appendleft())
# 2.examples using the print statement on line 15
# eg1. nums = [1,2,3,4,5,6,7], k = 3
# deque([1])
# deque([2])
# deque([3])
# deque([4])
# deque([5])
# deque([6])
# eg2. nums = [-1,-2,-3,-4,-5,-6,-7], k = 3
# deque([0, 1])
# deque([0, 1, 2])
# deque([0, 1, 2, 3])
# deque([1, 2, 3, 4])
# deque([2, 3, 4, 5])
# deque([3, 4, 5, 6])
