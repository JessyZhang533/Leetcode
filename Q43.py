# Path sum

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 1. For a recursively called function f1, we may call f1(a) then f1(b) then f1(c), but if f1(c) returns true, f1(b) or f1(a) wouldn't just automatically return true
    def hasPathSum_1(self, root, targetSum: int) -> bool:
        if root is None:  # !!! edge case: tree is empty
            return False
        sum = root.val
        def traverse(sum, curr_node):
            if curr_node.left:
                sum += curr_node.left.val
                if traverse(sum, curr_node.left):  # 1.
                    return True
                sum -= curr_node.left.val  # !!! recover sum
            if curr_node.right:
                sum += curr_node.right.val
                if traverse(sum, curr_node.right):  # 1.
                    return True
                sum -= curr_node.right.val  # !!! recover sum
            if curr_node.left is None and curr_node.right is None and sum == targetSum:
                return True

        if traverse(sum, root):
            return True
        else:
            return False

    def hasPathSum_2(self, root, targetSum):  # In this function root is a pointer, can point to other nodes
        if not root:  # node is empty
            return False

        if not root.left and not root.right and root.val == targetSum:  # base case
            return True
        
        targetSum -= root.val  # Instead of adding up nodes to see if equals to targetsum, reduce targetsum to see if it equals to node value instead

        return self.hasPathSum_2(root.left, targetSum) or self.hasPathSum_2(root.right, targetSum)  # This is true when at least one of the functions returns true


root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
solution = Solution()
print(solution.hasPathSum_2(root, 22))