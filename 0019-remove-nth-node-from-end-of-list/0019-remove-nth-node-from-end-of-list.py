# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head1: Optional[ListNode], n: int) -> Optional[ListNode]:
        h=head1
        c=0
        while(h!=None):
            c+=1
            h=h.next
        k=c-n+1
        #print(c,k,n)
        if c==1 and n==1:
            return None
        c=0
        h=head1
        while(h!=None):
            c+=1
            if c==k-1:
                #print(c,k-1)
                h.next=h.next.next
                break
            h=h.next
        if k==1:
            return head1.next
        return head1
            
            
        