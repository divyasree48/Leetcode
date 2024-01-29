# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        def fun(prev,temp,nex):
            if nex==None:
                
                temp.next=prev
                return temp
            #print(temp.val)
            temp.next=prev
            prev=temp
            temp=nex
            #print(temp.val)
            nex=temp.next
            
            return fun(prev,temp,nex)
            
        return fun(None,head,head.next)
        
        