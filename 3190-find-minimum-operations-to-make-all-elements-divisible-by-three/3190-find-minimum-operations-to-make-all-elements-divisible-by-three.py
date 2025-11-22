class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            m = i%3
            c += min(m,3-m)
        return c
        