class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(target, index, path):  # does Not return anything, only function is updating 'res'
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):  # current index included, because the same entry can be used multiple times
                dfs(target-candidates[i], i, path+[candidates[i]])  # can use + or extend, but cannot use append.
                # This is because of the memory allocation. When you are calling func(path + [nums[i]]), you are assigning path + [nums[i]] to the path of the next recursion without changing the memory of the path of the current recursion, which is to be used repeatedly in the for loop.
                # If you use append, you will change the CURRENT path and it is not desired.
        dfs(target, 0, [])
        return res
