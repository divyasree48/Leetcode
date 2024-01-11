# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        def fun(root):
            if root==None:
                return [-1,-1]
            if root.left==None and root.right==None:
                return [root.val,root.val]
            a=fun(root.left)
            b=fun(root.right)
            if a==[-1,-1]:
                x=[abs(root.val-max(b[0],b[1])),abs(root.val-min(b[0],b[1]))]
                ans[0]=max(ans[0],max(x))
                return [max(root.val,b[0]),min(root.val,b[1])]
            if b==[-1,-1]:
                x=[abs(root.val-max(a[0],a[1])),abs(root.val-min(a[0],a[1]))]
                ans[0]=max(ans[0],max(x))
                return [max(root.val,a[0]),min(root.val,a[1])]
            x=[abs(root.val-max(a[0],a[1],b[0],b[1])),abs(root.val-min(a[0],a[1],b[0],b[1]))]
            ans[0]=max(ans[0],max(x))
            return [max([root.val,a[0],b[0]]),min([root.val,a[1],b[1]])]
        p=fun(root)
        return ans[0]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     