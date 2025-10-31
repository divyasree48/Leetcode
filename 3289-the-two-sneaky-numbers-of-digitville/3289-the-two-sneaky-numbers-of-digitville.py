class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            if d[i] > 1:
                ans.append(i)
        return ans
        