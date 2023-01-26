# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0  # 'self.' is needed to create a 'global' variable
        def dfs(p):
            if not p:
                return 0
            left, right = dfs(p.left), dfs(p.right)  # firstly will go all the way down dfs(p.left)
            self.res = max(self.res, left+right)
            return 1 + max(left, right)  # this is a value ready to be assigned to 'left' or 'right'
        dfs(root)
        return self.res
