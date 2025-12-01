class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left,right = 0, sum(batteries)
        while left < right:
            m = (left + right + 1) >> 1
            total = 0
            for i in batteries:
                total += min(i,m)
            if total >= n*m:
                left = m
            else:
                right = m-1
        return left
        