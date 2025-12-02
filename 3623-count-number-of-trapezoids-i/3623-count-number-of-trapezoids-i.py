class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        d = defaultdict(int)
        mod = 1000000007
        res = 0
        s = 0
        for i in points:
            d[i[1]] += 1
        for i in d.values():
            a = i * (i-1) // 2
            res = (res + a * s) % mod
            s = (s + a) % mod
        return res
        