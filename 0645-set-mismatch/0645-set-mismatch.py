class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        d={}
        n=len(nums)
        d[nums[0]]=1
        s=nums[0]
        for i in range(1,n):
            if nums[i] in d.keys():
                x=nums[i]
            else:
                d[nums[i]]=1
                s+=nums[i]
        b=(n*(n+1))//2
        return [x,b-s]
            
        
        