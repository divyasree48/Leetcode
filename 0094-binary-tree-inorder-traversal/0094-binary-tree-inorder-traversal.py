# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def fun(root):
            if root==None:
                return
            fun(root.left)
            l.append(root.val)
            fun(root.right)
        if root==None:
            return []
        if root.left==None and root.right==None:
            return [root.val]
        fun(root)
        return l
        