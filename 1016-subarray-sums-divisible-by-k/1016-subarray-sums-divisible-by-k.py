class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre=ans=0
        d={}
        d[0]=1
        for i in nums:
            pre+=i
            a=pre%k
            if a<0:
                a+=k
            if a in d.keys():
                ans+=d[a]
                d[a]+=1
            else:
                d[a]=1
        return ans
        