class Solution:
    def maxProduct(self, A: List[int]) -> int:  # t.c. O(N)
        " Calculate the prefix and suffix products of A "
        B = A[::-1]  # B is the reverse of A
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1  # if A[i]*A[i-1]=0, then execute A[i] *= 1
            B[i] *= B[i - 1] or 1
        return max(A + B)  # !!! A+B returns a list with all elemnts of A and B (elements of A in the front)
        # Basic Idea:
        # First, if there's no zero in the array, then the subarray with maximum product must start with the first element or end with the last element. 
        # And therefore, the maximum product must be some prefix product or suffix product. So in this solution, we compute the prefix product A and suffix product B, and simply return the maximum of A and B.
        # What if there are zeroes in the array? Well, we can split the array into several smaller ones. That's to say, when the prefix product is 0, we start over and compute prefix profuct from the current element instead.
        # And this is exactly what A[i] *= (A[i - 1]) or 1 does.
