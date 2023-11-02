class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def BST(root,ans):
            if root == None:
                return (0,0)
            left = BST(root.left,ans)
            right = BST(root.right,ans)
            sumofval = left[0] + right[0] + root.val
            count = left[1]+right[1]+1
            if count != 0 and sumofval//count == root.val:
                ans[0]+=1
            return sumofval,count
        BST(root,ans)
        return ans[0]