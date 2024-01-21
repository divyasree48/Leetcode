class Solution:
    def rob(self, l: List[int]) -> int:
        prev=cur=0
        for i in l:
            temp=max(prev+i,cur)
            prev=cur
            cur=temp
        return cur