class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        c=0
        maxi=-1
        for i in nums:
            if i<c:
                maxi=max(maxi,i+c)
            c+=i
        return maxi
        