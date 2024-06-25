# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        cur = [0]
        def dfs(root):
            if not root:
                return 
            dfs(root.right)
            cur[0] += root.val
            root.val = cur[0]
            dfs(root.left)
        dfs(root)
        return root
            