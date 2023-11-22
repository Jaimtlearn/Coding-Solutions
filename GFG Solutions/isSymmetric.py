class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        # Your Code Here
        if not root:
            return True
        def Mirror(ptrl,ptrr):
            if not ptrl and not ptrr:
                return True
            if not ptrl or not ptrr:
                return False
            if ptrl.data != ptrr.data:
                return False
            return Mirror(ptrl.left,ptrr.right) and Mirror(ptrl.right,ptrr.left)
        
        return Mirror(root.left,root.right)
