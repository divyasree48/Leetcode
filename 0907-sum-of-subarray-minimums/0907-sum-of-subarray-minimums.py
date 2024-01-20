class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        mod=1000000007
        n=len(nums)
        left=[None]*n
        right=[None]*n
        s1=[]
        s2=[]
        for i in range(n):
            cnt=1
            while len(s1)>0 and s1[-1][0]>nums[i]:
                cnt+=s1[-1][1]
                s1.pop()
            left[i]=cnt
            s1.append([nums[i],cnt])
        for i in range(n-1,-1,-1):
            cnt=1
            while(len(s2)>0 and s2[-1][0]>=nums[i]):
                cnt+=s2[-1][1]
                s2.pop()
            right[i]=cnt
            s2.append([nums[i],cnt])
            #print(cnt)
        #print(left,right)
        ans=0
        for i in range(n):
            c=(nums[i]%mod)*(right[i]%mod)*(left[i]%mod)
            ans+=(c%mod)
            ans=ans%mod
        return ans
            
            
        