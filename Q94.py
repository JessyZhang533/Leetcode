# Binary Tree inorder trasversal

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res_list = []
        if root is None:  # !!! Edge Case
            return res_list
        
        def traverse(curr_node):
            if curr_node.left:
                traverse(curr_node.left)
            res_list.append(curr_node.val)
            if curr_node.right:
                traverse(curr_node.right)

        traverse(root)
        return res_list