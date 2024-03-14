class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n=len(nums)
        ans=(n*(n+1))//2
        if len(set(nums))==1:
            if goal==0:
                if nums[0]==0:
                    return ans
                else:
                    return 0
            elif goal==1:
                if nums[0]==1:
                    return ans
                else:
                    return 0
            
        l=[0]
        d={}
        d[0]=1
        ans=0
        for i in nums:
            k=l[-1]+i
            l.append(k)
            if k-goal in d.keys():
                ans+=d[k-goal]
            if k in d.keys():
                d[k]+=1
            else:
                d[k]=1
        return ans
        
        