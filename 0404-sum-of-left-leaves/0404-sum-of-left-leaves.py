# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        l=[]
        def fun(root,ind):
            if root==None:
                return
            if root.left==None and root.right==None:
                if ind:
                    l.append(root.val)
                return
            fun(root.left,1)
            fun(root.right,0)
            
        fun(root,0)
        #print(l)
        return sum(l)
        