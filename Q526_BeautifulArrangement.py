class Solution:
    def countArrangement_1(self, n: int) -> int:  # time limit exceeded
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