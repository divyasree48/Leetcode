# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def fun(root,a,b):
            if root==None:
                return 0
            if root.val<=b and root.val>=a:
                return root.val+fun(root.left,a,b)+fun(root.right,a,b)
            else:
                return fun(root.left,a,b)+fun(root.right,a,b)
        return fun(root,low,high)
        
        