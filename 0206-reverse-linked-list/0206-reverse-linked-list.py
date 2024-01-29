# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        prev=None
        temp=head
        nex=head.next
        while(nex!=None):
            #print(temp.val)
            
            temp.next=prev
            prev=temp
            temp=nex
            nex=temp.next
        temp.next=prev
        
        return temp
        