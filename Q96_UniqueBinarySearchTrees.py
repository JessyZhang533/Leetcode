# KEY: https://leetcode.com/problems/unique-binary-search-trees/solutions/1565543/c-python-5-easy-solutions-w-explanation-optimization-from-brute-force-to-dp-to-catalan-o-n/
# Now, we need to realize that the number of structurally unique BST formable with nodes having value i+1...n is
# equal to the number of structurally unique BST formable with nodes having value i+1-i...n-i = 1...n-i.
# Why? Because we only need to find BST which are structurally unique irrespective of their values and
# we can form an equal number of them with nodes from 1...n or 2...n+1 or n...2n-1 and so on.
# So, the number only depends on number of nodes using which BST is to be formed.
# Now, when we choose i as root node, we will have nodes from 1...i-1 (i-1 nodes in total) in left sub-tree
# and nodes from i+1...n (n-i nodes in total) in the right side. We can then form numTrees(i-1) BSTs for left
# sub-tree and numTrees(n-i) BSTs for the right sub-tree. The total number of structurally unique BSTs formed
# having root i will be equal to product of these two, i.e, numTrees(i-1) * numTrees(n-i).
# The same can be followed recursively till we reach base case - numTrees(0) = numTrees(1) = 1 because we can
# form only a single empty BST and single node BST in these cases respectively.

class Solution:
    def numTrees_1(self, n: int) -> int:
        " Direct recursive (top down); time limit exceeded "
        if n <= 1: return 1
        return sum(self.numTrees(i-1) * self.numTrees(n-i) for i in range(1, n+1))

    def numTrees_2(self, n: int) -> int:
        " dp "
        dp = [0]*(n+1)  # dp[i] is the num of BSTs formed using n nodes (0 node: 1 empty tree)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]