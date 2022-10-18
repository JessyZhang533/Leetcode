# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS: use while loop and the concept of queue
from collections import deque  # !!!: queue
class Solution:
    def levelOrder_1(self, root):
        if not root:
            return []
        queue, res = deque([root]), []

        while queue:  # Here we need a for loop in the while loop to group all values on teh same level
            cur_level, size = [], len(queue)
            for _ in range(size):
                node = queue.popleft()
                cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur_level)
        return res

    def levelOrder_2(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])            
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans
