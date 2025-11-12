class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        c = nums.count(1)
        if c > 0:
            return n - c
        mini = n + 1
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur = gcd(cur, nums[j])
                if cur == 1:
                    l = j - i + 1
                    mini = min(mini, l)
                    break
        if mini > n:
            return -1
        return n - 1 + mini - 1
        