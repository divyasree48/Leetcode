class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval: (interval[1],-interval[0]))
        last = -1
        first = -1
        res = 0
        for st,end in intervals:
            if st <= last:
                continue
            if st > first:
                res += 2
                last = end - 1
                first = end
            else:
                res += 1
                last = first
                first = end
        return res
        