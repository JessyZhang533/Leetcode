class Solution:
    def countArrangement_1(self, n: int) -> int:  # time limit exceeded
        " First find all permutations, then check each one to see if satisfies requirements "
        def permutation(list):
            " Return all permutations of a list "
            result = []
            # base case
            if len(list) == 1:
                return [list[:]]
            for _ in range(len(list)):
                n = list.pop(0)
                perms = permutation(list)
                for perm in perms:
                    perm.append(n)
                result.extend(perms)
                list.append(n)
            return result

        def check(perm):
            for i in range(len(perm)):
                if not perm[i] % (i+1):
                    if i == len(perm) - 1:
                        return True
                    else:
                        continue
                elif not (i+1) % perm[i]:
                    if i == len(perm) - 1:
                        return True
                    else:
                        continue
                else:
                    return False

        list_n = list(range(1, n+1))
        list_permutations = permutation(list_n)
        count = 0
        for perm in list_permutations:
            if check(perm):
                count += 1
            else:
                continue
        return count

    def countArrangement_2(self, n: int) -> int:
        def check(i, X):
            if i == 1:
                return 1
            # 1. for...if... statesments below: check if the (i-1)th element (0 indexed) of the permutation satisfies one of the two the requirement
            # 2. Check from higher index to lower index can trim down the number of operations.
            # If we check from count(0, X - {x}), then no matter what 'x' we choose to pop in our first step, the requirement will always be fulfilled, hence we cannot discard any potential misfit
            # 3. Reason we use set instead of list: use '-' to update the iterable
            return sum(check(i - 1, X - {x}) for x in X if x % i == 0 or i % x == 0)  # '{}' means 'set' here
        return check(n, set(range(1, n + 1)))
