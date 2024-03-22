# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return head
        first=head
        f=head
        s=head
        l=[]
        while(s!=None and s.next!=None):
            l.append(f.val)
            prev=f
            f=f.next
            s=s.next.next
        prev.next=None
        t=None
        second=None
        while(f!=None):
            nxt=f.next
            f.next=t
            t=f
            second=t
            f=nxt
        while(first!=None and second!=None):
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True
        
        
        
        