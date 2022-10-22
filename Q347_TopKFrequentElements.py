class Solution:
    def topKFrequent_1(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return None
        dic = {}
        res = []
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            
        value_list = list(dic.values())
        value_list.sort()
        k_most_f = value_list[-k:]
        for j in dic:
            if dic[j] in k_most_f:
                res.append(j)
        return res

    # 1.Counter: https://docs.python.org/3/library/collections.html#collections.Counter
    # 2.Difference between dic and defaultdic: https://realpython.com/python-defaultdict/
    def topKFrequent_2(self, nums, k):
        frq = defaultdict(list)
        for key, cnt in Counter(nums).items():
            frq[cnt].append(key)  # count as the key (sacrifice space complexity for time complexity)

        res = []
        for times in reversed(range(len(nums) + 1)):
            res.extend(frq[times])
            if len(res) >= k: return res[:k]

        return res[:k]
