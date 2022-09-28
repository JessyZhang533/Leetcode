# Root equals sum of children
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree_1(self, root: Optional[TreeNode]) -> bool:
        if root.val == root.left.val + root.right.val:
            return True
        return False

    # One line solution
    def checkTree_2(self, root: Optional[TreeNode]) -> bool:
        return root.val == (root.left.val + root.right.val)  # Since the function returns only True or False, we can return a boolean
