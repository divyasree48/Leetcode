class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(0,len(nums)+1):
            c=0
            for j in nums:
                if j>=i:
                    c+=1
            if c==i:
                return c
        return -1
        