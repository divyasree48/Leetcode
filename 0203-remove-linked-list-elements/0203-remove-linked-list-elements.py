# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head==None:
            return head
        if head.next==None:
            if head.val==val:
                return None
            return head
        ans=head
        t1=None
        t2=head
        while(t2):
            if t2.next==None:
                if t2.val==val:
                    if t1!=None:
                        t1.next=None
                    else:
                        ans=None
                t2=t2.next
            else:
                if(t2.val==val):
                    if t1==None:
                        t1=t2.next
                        ans=t1
                        t2.next=None
                        t2=t1
                        t1=None
                    else:
                        x=t2.next
                        t1.next=t2.next
                        t2=x
                else:
                    
                    t1=t2
                    t2=t2.next
        return ans
                        
        
        