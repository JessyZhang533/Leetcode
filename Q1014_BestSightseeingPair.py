class Solution:
    def maxScoreSightseeingPair_1(self, values: List[int]) -> int:
        # https://leetcode.com/problems/best-sightseeing-pair/solutions/260850/java-c-python-one-pass-o-1-space/
        best_prev_score, res = 0, 0  # best_prev_score is the current best score in all previous sightseeing spot. ('current' means w.r.t. the current entry in the for loop in list values)
        for i in values:
            res = max(res, best_prev_score + i)
            best_prev_score = max(best_prev_score, i) - 1  # -1 because we're preparing this value for tyhe next iteration
        return res

    def maxScoreSightseeingPair_2(self, values: List[int]) -> int:
        # A: list of values[i]+i
        # B: list ofvalues[j]-j
        # Now the question is: find max(A[a]+B[b]) for all a<b
        A, B = [], []
        for i in range(len(values)):
            A.append(values[i]+i)
        for j in range(len(values)):
            B.append(values[j]-j)
        # !!! the following code
        res = 0
        best_prev = A[0]
        for b in range(1, len(B)):  # 'move one pointer steadily using a for loop'
            res = max(res, best_prev + B[b])
            best_prev = max(best_prev, A[b])
        return res

    def maxScoreSightseeingPair_3(self, values: List[int]) -> int:
        # https://leetcode.com/problems/best-sightseeing-pair/solutions/1521786/very-easy-explanation-dp-complexity-analysis-python/
        dp = [0]*(len(values))
        dp[0] = values[0]
        res = 0
        for i in range(1, len(values)):
            dp[i] = max(dp[i-1], values[i-1]+i-1)  # equivcalent to A & best_prev in method 2
            res = max(res, dp[i]+values[i]-i)  # equivalent to B & res
        return res
