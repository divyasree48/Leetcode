class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        rem = Counter(i % value for i in nums)
        for i in range(len(nums) + 1):
            if rem[i % value] == 0:
                return i
            rem[i % value] -= 1

        