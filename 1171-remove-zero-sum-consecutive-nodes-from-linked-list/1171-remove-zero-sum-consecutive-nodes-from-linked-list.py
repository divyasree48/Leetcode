# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        h=head
        while(h!=None):
            l.append(h.val)
            h=h.next
        i=0
        while(i<len(l)):
            c=l[i]
            
                
            j=i+1
            while(j<=len(l)):
                if c==0:
                    a=l[:i:]
                    b=l[j::]
                    l=a+b
                    i=-1
                    #print(a,b,l)
                    break
                if j<len(l):    
                    c+=l[j]
                j+=1
                #print(l)
            i+=1
            
        #print(l)
        ans=ListNode()
        t=ans
        for i in l:
            t.next=ListNode(i)
            t=t.next
        return ans.next
                    