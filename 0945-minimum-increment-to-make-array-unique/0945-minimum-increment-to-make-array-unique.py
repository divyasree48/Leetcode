class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        k=nums[0]
        ans=0
        for i in nums:
            if i<k:
                ans+=k-i
            else:
                k=i
            k+=1
        return ans
        