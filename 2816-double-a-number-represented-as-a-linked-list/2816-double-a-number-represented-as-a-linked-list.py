# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
sys.set_int_max_str_digits(100000)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        s=''
        while(t!=None):
            s+=str(t.val)
            t=t.next
        x=int(s)*2
        a=str(x)
        t=ListNode()
        x=t
        for i in a:
            b=ListNode(int(i))
            x.next=b
            x=b
        return t.next
        