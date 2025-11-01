# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums.sort()
        n=len(nums)
        temp=ListNode(0)
        temp.next=head
        cur=temp
        while cur.next!=None:
            i=bisect.bisect_left(nums,cur.next.val)
            if i<n and nums[i]==cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return temp.next
            
        