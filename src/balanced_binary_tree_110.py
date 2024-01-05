# Given a binary tree, determine if it is height-balanced.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        if root is None:
            return True
        
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
