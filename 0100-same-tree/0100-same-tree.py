# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l=[]
        m=[]
        def fun1(p,l):
            if p==None:
                l.append(999999)
                return
            
            l.append(p.val)
            fun1(p.left,l)
            fun1(p.right,l)
        def fun2(q,m):
            if q==None:
                m.append(999999)
                return
            
            m.append(q.val)
            fun2(q.left,m)
            fun2(q.right,m)
        fun1(p,l)
        fun2(q,m)
        #print(l,m)
        if l==m:
            return True
        return False