# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1=l1
        h2=l2
        a=k=0
        while(h1!=None):
            a+=(h1.val*(10**k))
            k+=1
            h1=h1.next
        b=k=0
        while(h2!=None):
            b+=(h2.val*(10**k))
            k+=1
            h2=h2.next
        c=a+b
        #print(c)
        if c==0:
            ans=ListNode(0)
            return ans
        head=None
        temp=None
        while(c):
            r=c%10
            x=ListNode(r)
            if head==None:
                head=x
                temp=head
            else:
                head.next=x
                head=head.next
            head.val=r
            c=c//10
        return temp
            
            
        