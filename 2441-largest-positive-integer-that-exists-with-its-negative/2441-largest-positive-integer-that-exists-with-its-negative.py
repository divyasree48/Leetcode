class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        nums=nums[::-1]
        for i in nums:
            if -1*i in nums:
                return abs(i)
        return -1
        