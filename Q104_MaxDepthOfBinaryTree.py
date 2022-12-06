# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth_1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        list_count = []
        def dfs(curr_node, count):
            if curr_node.left:
                dfs(curr_node.left, count+1)
            if curr_node.right:
                dfs(curr_node.right, count+1)
            if (not curr_node.left) and (not curr_node.right):
                list_count.append(count)
        dfs(root, 1)
        return max(list_count)

    def maxDepth_2(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth  # !!!
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                       
        return dfs(root, 0)
