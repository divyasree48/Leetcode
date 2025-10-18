class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        ans = 0
        prev = -math.inf
        for i in sorted(nums):
            if prev < i + k:
                prev = max(prev + 1, i - k)
                ans += 1
        return ans
        