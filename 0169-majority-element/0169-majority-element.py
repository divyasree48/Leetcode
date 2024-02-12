class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        for i in nums:
            if i in d.keys():
                d[i]+=1
                if d[i]>n//2:
                    return i
            else:
                d[i]=1
                if d[i]>n//2:
                    return i