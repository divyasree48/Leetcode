# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while(head!=None):
            if head.val==999999:
                return 1
            head.val=999999
            head=head.next
        return 0
        