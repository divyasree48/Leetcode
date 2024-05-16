# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def fun(root):
            if root.left==None and root.right==None:
                return root.val
            a=fun(root.left)
            b=fun(root.right)
            if root.val==2:
                return a|b
            if root.val==3:
                return a&b
        return fun(root)
        