class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == original:
                original = nums[i] * 2
                i = 0
            else:
                i += 1
            if i == n:
                break
        return original
        