# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans=[]
        def fun(root,s,l):
            s+=chr(root.val+97)
            if root.left==None and root.right==None:
                l.append(s[::-1])
                return
            if root.left!=None:
                fun(root.left,s,l)
                s=s[:len(s):]
            if root.right!=None:
                fun(root.right,s,l)
                s=s[:len(s):]
            
        s=''
        l=[]
        fun(root,s,l)
        l.sort()
        #print(l)
        return l[0]
            
        