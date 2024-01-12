# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        def fun(root):
            if root==None:
                return [0,0]
            a=fun(root.left)
            b=fun(root.right)
            if a[0]==root.val and b[0]==root.val:
                ans[0]=max(ans[0],a[1]+b[1]+1)
                return [root.val,max(a[1],b[1])+1]
            elif a[0]==root.val:
                ans[0]=max(ans[0],a[1]+1)
                return [root.val,a[1]+1]
            elif b[0]==root.val:
                ans[0]=max(ans[0],b[1]+1)
                return [root.val,b[1]+1]
            else:
                ans[0]=max(ans[0],1)
                return [root.val,1]
        p=fun(root)
        if ans[0]==0:
            return 0
        return ans[0]-1
                
        