class Solution:
    def findShortestSubArray_1(self, nums: List[int]) -> int:
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                dic[n].append(i)
            else:
                dic[n] = [i]
        indices = sorted(list(dic.values()), key=len)
        print(indices)
        if len(indices[-1]) == 1:
            return 1
        res = indices[-1][-1] - indices[-1][0] + 1
        print(res)
        if len(indices) < 2:  # NOTE EDGE CASE
            return res
        for j in range(len(indices)-2, -1, -1):
            if len(indices[j]) < len(indices[-1]):
                return res
            else:
                res = min(res, indices[j][-1] - indices[j][0] + 1)
        return res

    def findShortestSubArray_2(self, A):  # t.c. O(N)
        first, count, res, degree = {}, {}, 0, 0
        # dic first: key-numbers; value-first index of occurence
        # dic count: key-numbers; value-number of occurrences
        for i, a in enumerate(A):
            first.setdefault(a, i)
            count[a] = count.get(a, 0) + 1
            if count[a] > degree:
                degree = count[a]
                res = i - first[a] + 1
            elif count[a] == degree:
                res = min(res, i - first[a] + 1)
        return res
        # 1. dictionary.get(): returns the value for the specified key if the key is in the dictionary.
        # get() method takes maximum of two parameters:
        # key - key to be searched in the dictionary
        # value (optional) - Value to be returned if the key is not found. The default value is None.
        # 2. dictionary.setdefault(): The setdefault() method returns the value of the item with the specified key.
        # If the key does not exist, insert the key with the specified value (2nd argument)
