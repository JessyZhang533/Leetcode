class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition of as valid BST: ALL nodes on the LHS of a node should be less than its value; vice versa for right
class Solution:
    def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):  # float('-inf') or float('inf'): representing infinity
        " Floor & ceiling "
        if not root: 
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)
