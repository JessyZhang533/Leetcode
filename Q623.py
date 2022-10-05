# Add one row to tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy, dummy.left = TreeNode(None), root  # dummy node: node of which depth is 0
        row = [dummy]
        for _ in range(depth - 1):
            row = [kid for node in row for kid in (node.left, node.right) if kid]  # !!!: if 'node' in the list 'row' has children, let 'row' be the list of children
        # After the first for loop, the row is a list of nodes at (depth-1)
        for node in row:
            node.left, node.left.left = TreeNode(val), node.left
            node.right, node.right.right = TreeNode(val), node.right
        return dummy.left
