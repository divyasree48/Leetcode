class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            x = nums[i]
            y = nums[i+1]
            if y % 2 == x % 2:
                return 0
        return 1