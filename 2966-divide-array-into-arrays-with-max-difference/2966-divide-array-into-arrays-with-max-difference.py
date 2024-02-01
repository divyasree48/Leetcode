class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums=sorted(nums)
        n=len(nums)
        b=[]
        for i in range(1,n,3):
            if nums[i]-nums[i-1]<=k and nums[i+1]-nums[i-1]<=k and nums[i+1]-nums[i]<=k:
                c=nums[i-1:i+2]
                b.append(c)
            else:
                return []
        return b