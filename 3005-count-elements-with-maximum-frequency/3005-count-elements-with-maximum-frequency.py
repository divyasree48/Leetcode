class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        mx=0
        for i in d.keys():
            if d[i]>mx:
                mx=d[i]
        ans=0
        for i in d.values():
            if i==mx:
                ans+=i
        return ans