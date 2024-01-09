# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def fun(root,l):
            if root==None:
                return 
            if root.left==None and root.right==None:
                l.append(root.val)
            fun(root.left,l)
            fun(root.right,l)
        a=[]
        b=[]
        fun(root1,a)
        fun(root2,b)
        print(a,b)
        if a==b:
            return 1
        return 0
        
        