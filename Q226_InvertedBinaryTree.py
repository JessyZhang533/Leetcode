# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree_1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if root.left and root.right:
            temp = root.left
            root.left = root.right
            root.right = temp
        elif root.left and not root.right:
            root.right = root.left
            root.left = None
        elif root.right and not root.left:
            root.left = root.right
            root.right = None
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root

    def invertTree_2(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
