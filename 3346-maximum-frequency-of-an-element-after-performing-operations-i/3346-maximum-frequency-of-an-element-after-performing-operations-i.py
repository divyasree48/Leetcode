class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        maxi = max(nums) + k + 2
        d = [0] * maxi
        for i in nums:
            d[i] += 1
        for i in range(1, maxi):
            d[i] += d[i - 1]

        res = 0
        for i in range(maxi):
            left = max(0, i - k)
            right = min(maxi - 1, i + k)
            total = d[right] - (d[left - 1] if left else 0)
            c = d[i] - (d[i - 1] if i else 0)
            res = max(res, c + min(numOperations, total - c))

        return res

        