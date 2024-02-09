class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        dp=[0]*n
        for i in range(n-1,-1,-1):
            k=0
            for j in range(i+1,n):
                if nums[j]%nums[i]==0:
                    k=max(k,dp[j]+1)
            dp[i]=k
        k=max(dp)
        ind=dp.index(k)
        ans=[nums[ind]]
        for i in range(ind+1,n):
            if k-dp[i]==1:
                if nums[i]%ans[-1]==0:
                    ans.append(nums[i])
                    k-=1
        return ans