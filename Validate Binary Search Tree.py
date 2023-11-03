class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def BST(root,Min,Max):
            if root == None:
                return True
            if root.val <= Min or root.val >= Max:
                return False
            left = BST(root.left,Min,root.val)
            right = BST(root.right,root.val,Max)
            return left and right
        
        return BST(root,float('-inf'),float('inf'))